# my_client.py
"""
Custom MCP client for the predict_both assignment.

Discovers available MCP tools, trains the models,
tests all 114 patients, and compares predictions.
"""

import asyncio

from agents.mcp import MCPServerStdio
from mcp_client_demo import params, call


async def main():

    async with MCPServerStdio(
        params=params,
        client_session_timeout_seconds=120
    ) as server:

        # STEP 1: Discover MCP tools

        tools = await server.list_tools()

        print(f"\nFound {len(tools)} tools:")

        for tool in tools:
            print(" -", tool.name)

        # STEP 2: Train both models

        print("\nTraining models...")

        await call(
            server,
            "train_models",
            {"request_id": "hw-train"}
        )

        # STEP 3: Compare predictions for 114 patients

        disagreements = []

        lr_correct = 0
        knn_correct = 0

        print("\nChecking all 114 test patients...\n")

        for i in range(114):

            sample = await call(
                server,
                "get_sample_input",
                {
                    "index": i,
                    "request_id": f"hw-sample-{i}"
                }
            )

            result = await call(
                server,
                "predict_both",
                {
                    "input_data": sample["input_data"],
                    "request_id": f"hw-both-{i}"
                }
            )

            if not result["models_agree"]:

                disagreements.append(i)

                true_class = sample["true_class"]

                lr_prediction = result["logistic_regression"]
                knn_prediction = result["knn"]

                if lr_prediction == true_class:
                    correct_model = "Logistic Regression"
                    lr_correct += 1

                elif knn_prediction == true_class:
                    correct_model = "KNN"
                    knn_correct += 1

                else:
                    correct_model = "Neither"

                print(
                    f"Patient {i}: "
                    f"True = {true_class}, "
                    f"LR = {lr_prediction}, "
                    f"KNN = {knn_prediction}, "
                    f"Correct = {correct_model}"
                )

        # STEP 4: Print final results

        print("\n===================================")
        print("FINAL RESULTS")
        print("===================================")

        print(f"Total test patients: 114")

        print(
            f"Models disagree on "
            f"{len(disagreements)} patients."
        )

        print(f"Disagreement patient indices: {disagreements}")

        print(
            f"Logistic Regression correct: {lr_correct}"
        )

        print(
            f"KNN correct: {knn_correct}"
        )

        if lr_correct > knn_correct:
            print("Better model on disagreements: Logistic Regression")

        elif knn_correct > lr_correct:
            print("Better model on disagreements: KNN")

        else:
            print("Both models performed equally on disagreements.")


if __name__ == "__main__":
    asyncio.run(main())