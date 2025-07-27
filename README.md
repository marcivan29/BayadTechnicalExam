# BayadTechnicalExam

Technical Exam

1. Run the MainAPI.py in vs code and download the missing extentions if needed.
2. In Postman, import the DigitalWallet.postman_collection
3. In the postman collection you can now test the each request.


Instructions for running the API

1. you need to use GenerateToken to all requests in 1 minute if the token expired you need to generate again.
2. I have existing user in the database for testing, if you want to create new user you can use Add User request.
3. In the Postman collection i have 3 requests
  - BalanceInquiry
    - Parameter: user_id and token
  - Cashin
    - Parameter: user_id, token and cashin amount
  - Debit
    - Parameter: user_id, token and debit amount
note: I set the token expiration to 1minute if the token expired you can generate again and use.
