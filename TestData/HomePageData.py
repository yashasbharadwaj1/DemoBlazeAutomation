class HomePageData:
    signup_data = [
        {"userName":"TesterOne","password":"tester"},
    ]

    positive_login_data = [
        # Positive scenario: Log in with valid credentials.
        {"userName": "TesterOne", "password": "tester"},
    ]

    negative_login_data = [
        # Negative scenario: Attempt to log in with invalid credentials.
        {"userName": "1", "password": "a"}
    ]
