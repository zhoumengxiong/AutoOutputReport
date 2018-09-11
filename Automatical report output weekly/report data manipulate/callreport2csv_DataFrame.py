# -*- coding: utf-8 -*-
import pandas as pd


def xlsx2csv(filename):
    call_report = pd.read_excel(filename)
    call_report = call_report.iloc[:, :121]
    call_report.insert(22, 'Level1Cause', '')
    call_report.to_csv(
        r"/mnt/hgfs/share2linux/callreport_week.csv",
        encoding='utf_8_sig',
        index=False)


if __name__ == '__main__':
    xlsx2csv(r"/mnt/hgfs/share2linux/callreport_week.xlsx")
