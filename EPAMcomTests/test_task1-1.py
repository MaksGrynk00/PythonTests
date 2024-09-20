
def test_check_title(browser, url1, expected_title="EPAM | Software Engineering & Product Development Services"):
    """Tests if the title of the provided URL matches the expected title."""
    browser.get(url1)
    actual_title = browser.title

    # Assert the actual title matches the expected title
    assert actual_title == expected_title, f"Title mismatch for {url1}. Expected: '{expected_title}', Actual: '{actual_title}'"