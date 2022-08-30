What is current url in selenium python
print(driver.current_url)
Source:stackoverflow.com

The current_url method is generally employed in cases where you require an intermediate URL from
a redirect chain or need to do a series of navigations among different URLs. This method is
ubiquitous in most situations involving browser automation.
Source: https://www.browserstack.com/guide/get-current-url-in-selenium-and-python#:~:text=The%20current_url%20method%20is%20generally,most%20situations%20involving%20browser%20automation.

You know very well that when you click on a link, you will be redirected to another page and that page has a url.
If clicking on that link does not fetch the required url, then something is wrong with the configuration.
You can use the Selenium webdriver "current_url" attribute which is a feature that fetches the current url of a web page.
When you click on a link, you will be redirected to the url of a page from that link.