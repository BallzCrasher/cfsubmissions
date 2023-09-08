def run(config: dict):

    # checks if submission satisfies config's parameters
    def check_submission(submission) -> bool:
        if not config['show_unrated'] and 'rating' not in submission['problem']:
            return False
        if 'rating' in submission['problem']:
            if config['min'] and submission['problem']['rating'] < config['min']:
                return False
            if config['max'] and submission['problem']['rating'] > config['max']:
                return False
        if config['verdict'] and submission['verdict'] != config['verdict']:
            return False
        return True

    # parsing response
    for submission in config['response']:
        if not check_submission(submission):
            continue
        contest = submission['problem']['contestId']
        sub_id = submission['id']
        print((submission['id'], submission['verdict'], submission['problem'],
            f"{config['BASE_URL']}/contest/{contest}/submission/{sub_id}"))
