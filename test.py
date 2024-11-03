def test_savings():
    from savings_account import create_savings_account

    results = create_savings_account(100, 15, 4)
    print(results)

def test_cd():
    from cd_account import create_cd_account

    results = create_cd_account(100, 30, 4)
    print(results)

# test_savings()
# test_cd()