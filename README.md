# Django QUIZ
## Technical requirements
### Web-UI
  1. Registration
      - [x] Registration (with email confirmation)
      - [x] Authorization
      - [x] Password change
      - [x] Passwor reset
    
  2. User capabilities
      - [ ] Passing any test
      - [ ] Sequentially answering test questions (one after another)
      - [ ] Finishing a deferred test
      - [ ] Removing an unfinished test
      - [ ] Viewing results
    
  3. After completing a test
      - [ ] Report on the number of correct and incorrect answers
      - [ ] Percentage of correct answers

### Admin site
  1. [ ] User management
  2. [ ] Test management
      - [ ] Adding a test
      - [ ] Modyfying a test
      - [ ] Deleting a test
      - [ ] Test validation
        - [ ] Can't save the question:
            - [ ] without indicating the correct answer
            - [ ] where all answers are correct
        - [ ] Can't save the test if:
            - [ ] incorrect order_num (should be from 1 to 100 and increase by 1)
            - [ ] the max value of order_num isn't more than the max allowable number of questions
            - [ ] the number of questions is less then 3 or more than 100

### Additional requirements
1. [x] The project must be on Git
2. [x] requirements.txt file
3. [x] venv
4. [ ] PostgreSQL
5. [ ] The presence of a data dump
6. [x] Bootstrap
7. [ ] Unit Tests
8. [ ] Docker image
9. [ ] Deployment on Amazon
10. [ ] Scheduler
11. [ ] Caching



ext.: [ ] API + Tests

