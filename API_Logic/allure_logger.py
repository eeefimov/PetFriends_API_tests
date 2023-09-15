import allure


class AllureLogger:
    def __init__(self, test_name):
        self.test_name = test_name
        self.logs = []

    def write(self, log):
        self.logs.append(log)

    def save_logs_to_allure(self):
        allure.attach('\n'.join(self.logs), name=f'Console Output for Test: {self.test_name}',
                      attachment_type=allure.attachment_type.TEXT)
