file = open("server.log")
error_count = 0
for line in file:
    if "error" in line.lower():
        print(line)
        error_count += 1
print("\nTotal Errors:", error_count)
with open("log_report.txt", "w") as f:
    f.write(f"Total Errors: {error_count}\n")
