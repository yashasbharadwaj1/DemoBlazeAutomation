class HomePageData:
    signup_data = [
        # this data helps to test both positive and negative case
        # first time test result is Signup successful.
        # second time result is This user already exist.
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
