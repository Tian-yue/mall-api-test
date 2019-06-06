import allure,pytest
from Common import Request, Assert, read_excel,Login

request = Request.Request()
assertions = Assert.Assertions()

url = Login.url
head = Login.Login().get_token()
yhq_id = 0
excel_list = read_excel.read_excel_list('./document/优惠券.xlsx')
ids_list = []
for i in range(len(excel_list)):
    # 删除excel_list中每个小list的最后一个元素,并赋值给ids_pop
    ids_pop = excel_list[i].pop()
    # 将ids_pop添加到 ids_list 里面
    ids_list.append(ids_pop)


@allure.feature('优惠券模块')
class Test_yhj:
    @allure.story('添加优惠券')


    def test_add_yhj(self):
        sel_yhq_resp = request.get_request(url=url+'coupon/list',
                                           params={'pageNum': 1, 'pageSize': 10}, headers=head)
        assertions.assert_code(sel_yhq_resp.status_code, 200)
        resp_json = sel_yhq_resp.json()
        assertions.assert_in_text(resp_json['message'], '成功')
        json_data = resp_json['data']
        data_list = json_data['list']
        item = data_list[0]
        global yhq_id
        yhq_id = item['id']
    @allure.story('删除优惠券')

    def test_del(self):
        del_yhq_resp = request.post_request(url=url + 'coupon/delete/' + str(yhq_id), headers=head)

        assertions.assert_code(del_yhq_resp.status_code, 200)
        resp_json = del_yhq_resp.json()
        assertions.assert_in_text(resp_json['message'], '成功')
