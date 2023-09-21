from parsel import Selector
html_text = """
<html>
<head>
    <title>Example Page</title>
</head>
<body>
    <div class="content">
        <h1>Hello, World!</h1>
        <p>This is a paragraph.</p>
    </div>
    <ul>
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
    </ul>
    <div class="image">
    <img src="example.jpg">
    <img src="picture.jpg" >
    </div>
    <a href="https://example.com">Link 1</a>
    <a href="https://pictures.com">Link 2</a>
    <ul class="_033281ab" style="columns:2" aria-label="Property details">
        <li>
            <span class="_3af7fa95">Type</span>
            <span class="_812aa185" aria-label="Type">Townhouse</span>
        </li>
        <li>
            <span class="_3af7fa95">Purpose</span>
            <span class="_812aa185">For Rent</span>
        </li>
        <li>
        <span class="_3af7fa95">Reference no.</span>
        <span class="_812aa185" aria-label="Reference">Bayut - 102164-g69R6d</span>
        </li>
    </ul>
</body>
</html>
"""
# Create a Selector object
selector = Selector(text=html_text)
title=selector.xpath('//title/text()').get()
h1=selector.xpath('//div[@class="content"]//h1/text()').get()
p=selector.xpath('//div[@class="content"]//p/text()').get()
li =selector.xpath('//ul/li/text()').get()
img=selector.xpath('//div[@class="image"]//img/@src').get()
img1=selector.xpath('//div[@class="image"]//img[2]/@src').get()
link = selector.xpath("//a[contains(@href, '://')]").getall()
purpose = selector.xpath('//span[@aria-label="Purpose"]/text()').get()
purpose2=selector.xpath('//ul[2]//li[2]/span[2]/text()').get()
purpose3=selector.xpath('//li/span[1]/text()').get()
purpose4=selector.xpath('//li[span[contains(text(), "Purpose")]]/following-sibling::li/span/text()').get()
type=selector.xpath('//*[contains(@class,"_033281ab")]//*[@aria-label="Purpose"]/text()').get()
type=selector.xpath('//*[contains(@class,"_033281ab")]/li[2]/span[2]/text()').get()
# test=selector.xpath('//div/*')
# print(title)
# print(h1)
# print(p)
# print(li)
# print(img)
# print(img1)
# print(test)
# print(link)
# print(type)
print(purpose)
print(purpose2)
print(purpose3)