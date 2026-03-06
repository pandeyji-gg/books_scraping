from playwright.async_api import async_playwright
import asyncio
import pandas as pd


async def run():
    async with async_playwright() as p:
        browser = await p.firefox.launch()
        page = await browser.new_page()

        await page.goto("https://books.toscrape.com")
        # Print title
        title = await page.title()
        print("the title is: ", title)

        data = []

        while True:
            books = page.locator("article.product_pod")
            count = await books.count()
            for i in range(count):
                book = books.nth(i)
                price = await book.locator("p.price_color").inner_text()
                title = await book.locator("h3 a").get_attribute("title")
                rating = await book.locator("p.star-rating").get_attribute("class")
                star_rating = rating.removeprefix("star-rating ").strip()
                data.append({"name": title, "price": price, "Star-rating": star_rating})
            next_btn = page.locator("li.next a")
            if await next_btn.count() == 0:
                break
            next_url = await next_btn.get_attribute("href")

            await page.goto(
                f"https://books.toscrape.com/catalogue/{next_url.split('/')[-1]}"
            )

        df = pd.DataFrame(data)
        print(df)
        df.to_csv("books.csv", index=False)

        await browser.close()


asyncio.run(run())
