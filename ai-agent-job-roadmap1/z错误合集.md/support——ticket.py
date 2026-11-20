class SupportTicket:
    def __init__(self, ticket_id, customer, issue, status):
        self.ticket_id = ticket_id
        self.customer = customer
        self.issue = issue
        self.status = status

    def show_info(self):
        print(f"工单编号：{self.ticket_id}")
        print(f"客户：{self.customer}")
        print(f"问题：{self.issue}")
        print(f"状态：{self.status}")
        print("")

    def resolve(self):
        self.status = "已解决"


support_ticket1 = SupportTicket("T001", "大科技公司", "api调用失败", "待处理")
support_ticket2 = SupportTicket("T002", "小科技公司", "网络请求失败", "待处理")

support_ticket1.resolve()

support_ticket1.show_info()
support_ticket2.show_info()