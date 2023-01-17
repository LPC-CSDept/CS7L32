def main():
    ##################################################
    # Comlete your code here
    ##################################################

    score = int(input('Enter your score'))

    if (score >= 90):
        print("Your score {0} is Grade {1}".format(score, 'A'))
    elif (score >= 80):
        print("Your score {0} is Grade {1}".format(score, 'B'))
    elif (score >= 70):
        print("Your score {0} is Grade {1}".format(score, 'C'))
    elif (score >= 60):
        print("Your score {0} is Grade {1}".format(score, 'D'))
    else:
        print("Your score {0} is Grade {1}".format(score, 'F'))
    pass


if __name__ == '__main__':
    main()
