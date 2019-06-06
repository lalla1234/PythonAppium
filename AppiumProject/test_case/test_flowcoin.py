from common.unittestFunc import UnittestFunc
from pageObject.communPage import CommunPage
from common.recordlog import logs
import unittest

class TestCommunPage(UnittestFunc):
    '''通信模块'''

    def test_flowcoin(self):
        '''流量币兑换正常'''
        comm = CommunPage(self.driver)
        num = comm.check_flow_exchange_successful()
        flow = comm.flow_coin()
        self.assertNotEqual(flow,num,'未兑换成功')

    @unittest.skip("skip test_flowcoin_err")
    def test_flowcoin_err(self):
        '''流量币兑换异常'''
        comm = CommunPage(self.driver)
        num = comm.check_flow_exchange_successful()
        flow = comm.flow_coin()
        self.assertEqual(flow, num, '未兑换成功')


if __name__ == '__main__':
    unittest.main()