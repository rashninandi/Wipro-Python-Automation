import json
from datetime import datetime


# =========================================================
# READ REPORT DATA
# =========================================================

with open("report_data.json", "r") as file:
    report = json.load(file)


# =========================================================
# CREATE HTML REPORT
# =========================================================

with open("execution_report.html", "w") as file:

    file.write("""
<html>

<head>

<title>Selenium Execution Report</title>

</head>

<body>

<h1>Selenium Automation Execution Report</h1>

<p>
<b>Execution Date:</b>
""" + str(datetime.now()) + """
</p>

<table border="1" cellpadding="10">

<tr>

<th>Step</th>

<th>Result</th>

</tr>
""")


    # Write each result into the table

    for item in report:

        file.write(
            "<tr>"
            "<td>" +
            item["step"] +
            "</td>"
            "<td>" +
            item["result"] +
            "</td>"
            "</tr>"
        )


    file.write("""
</table>

</body>

</html>
""")


print("Execution report generated successfully.")

print("File: execution_report.html")