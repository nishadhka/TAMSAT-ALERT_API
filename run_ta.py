import os



datelist=['20220820','20220825','20220830','20220901','20220905','20220910','20220915','20220920','20220925','20220930',
          '20221001','20221005','20221010','20221015','20221020','20221025','20221030','20221101','20221105','20221110',
          '20221115','20221120']


for datel in datelist[2:25]:
    os.mkdir('outputs')
    newcommand=f'python T-A_API.py {datel} 20221001 20221231 0.15 0.30 0.55 region 21.838949 51.415695 -11.745695 23.145147'
    os.system(newcommand)
    os.rename("outputs", datel)

