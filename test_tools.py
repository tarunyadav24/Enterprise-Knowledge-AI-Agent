from mcp_server.tools import (
    get_company_policy,
    get_holiday_calendar,
    search_documents,
)

print("\nCompany Policy\n")
print(get_company_policy())

print("\nHoliday Calendar\n")
print(get_holiday_calendar())

print("\nSearch Results\n")
print(search_documents("leave policy"))