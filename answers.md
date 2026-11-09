Assignment: Build and Call Your Own MCP Tool

Question 1: How many tools did the server list in Part 1, and how many in Part 3? What did you have to change in the client to make the new tool appear?

In Part 1, the MCP server listed 8 tools. After adding the predict_both function using the @server.tool() decorator, the server listed 9 tools.

I did not need to make any changes to the client to register the new tool. The MCP client automatically discovers available tools using server.list_tools(). Once the new tool was added to the server, it appeared in the tool list.

Question 2: On how many of the 114 test patients do the two models disagree? For each of those patients, which model was right?

After testing all 114 patients, Logistic Regression and KNN disagreed on 8 patients.

The results are shown below:

Patient Index	Actual Diagnosis	Logistic Regression	KNN	Correct Model
3	Benign	Benign	Malignant	Logistic Regression
25	Benign	Benign	Malignant	Logistic Regression
48	Benign	Benign	Malignant	Logistic Regression
53	Malignant	Benign	Malignant	KNN
76	Malignant	Malignant	Benign	Logistic Regression
80	Benign	Benign	Malignant	Logistic Regression
99	Benign	Benign	Malignant	Logistic Regression
102	Malignant	Malignant	Benign	Logistic Regression

The models disagreed on patients 3, 25, 48, 53, 76, 80, 99, and 102.

Question 3: Overall, which model was right more often when they disagreed?

Logistic Regression performed better when the two models disagreed.

Out of the 8 disagreements:

* Logistic Regression correctly predicted 7 patients.
* KNN correctly predicted 1 patient.

Logistic Regression was correct in 87.5% of the disagreement cases, while KNN was correct in 12.5%.

This shows that Logistic Regression performed better than KNN on the patients where their predictions differed.

Question 4: In your own words, why does the description in triple quotes ("""...""") matter when an AI app uses this tool?

The description inside triple quotes is called a docstring. It explains what the tool does and helps an AI application understand when to use it.

For example, the predict_both tool has a description explaining that it runs both machine learning models and checks whether their predictions agree.

When an AI application discovers the MCP tools, it can read their descriptions and decide which tool is appropriate for the user’s request.

Without clear descriptions, the AI might select the wrong tool or misunderstand its purpose.

Question 5: Why is it useful for the server to log every tool call?

Logging every tool call helps track what happened when the MCP server was used.

The audit log records information such as the request ID, tool name, execution status, and additional tool-specific details.

This is useful for debugging errors, monitoring tool usage, and verifying that the tools are working correctly.

In this project, the server stores audit records in a Parquet file. I verified that the log contained successful predict_both calls, including hw-both-109 through hw-both-113.

The audit log also provides a record of tool activity that can be reviewed later for troubleshooting and accountability.