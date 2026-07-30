
import asyncio

from mcp import ClientSession
from mcp import StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():

    server_params = StdioServerParameters(
        command="python",
        args=["server.py"],
    )

    async with stdio_client(server_params) as (read, write):

        async with ClientSession(read, write) as session:

            await session.initialize()

            while True:

                print("\n==============================")
                print("      AWO MCP Demo")
                print("==============================")
                print("1. Count facilities")
                print("2. Search by city")
                print("3. Search by service")
                print("0. Exit")

                choice = input("\nChoose: ").strip()

                if choice == "0":
                    print("Goodbye.")
                    break

                result = None

                if choice == "1":
                    city = input("City: ").strip()
                    if not city:
                        print("Please enter a city.")
                        continue
                    try:
                        result = await session.call_tool(
                            "count_facilities",
                            {"city": city}
                        )
                    except Exception as e:
                        print(f"\nError: {e}")
                        continue

                elif choice == "2":
                    city = input("City: ").strip()
                    if not city:
                        print("Please enter a city.")
                        continue
                    try:
                        result = await session.call_tool(
                            "search_facilities",
                            {"city": city}
                        )
                    except Exception as e:
                        print(f"\nError: {e}")
                        continue

                elif choice == "3":
                    service = input("Service: ").strip()
                    if not service:
                        print("Please enter a service.")
                        continue
                    try:
                        result = await session.call_tool(
                            "find_facilities_by_service",
                            {"service": service}
                        )
                    except Exception as e:
                        print(f"\nError: {e}")
                        continue

                else:
                    print("Invalid option.")
                    continue

                print("\n==============================")
                print("          RESULT")
                print("==============================")

                if result and result.content:
                    print(result.content[0].text)
                else:
                    print("No response returned.")

                print("\nPress Enter to continue...")
                input()


if __name__ == "__main__":
    asyncio.run(main())
