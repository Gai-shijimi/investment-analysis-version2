# new_pl_interest_coverage_ratio
""" インタレストカバレッジレシオ """


class InterestCoverageRatio:
    def __init__(self, operating_profit, interest_income, dividends_income, equity_in_net_income_of_affiliates,
                 interest_expense, effective_tax_rate):
        self.operating_profit = operating_profit  # 営業利益
        self.interest_income = interest_income  # 受取利息
        self.dividends_income = dividends_income  # 受取配当金
        self.e_i_n_i_o_a = equity_in_net_income_of_affiliates  # 持分法による投資損益
        self.interest_expense = interest_expense  # 支払利息
        self.effective_tax_rate = effective_tax_rate  # 実効税率

    def __gt__(self, sample2):
        if (self.operating_profit + self.interest_income + self.dividends_income + self.e_i_n_i_o_a) / \
                self.interest_expense \
                > sample2:
            return "一番目のサンプルの方が、二番目のサンプルより大きい値を示しています。"
        else:
            return "二番目のサンプルの方が、一番目のサンプルより大きい値を示しています。"

    def __lt__(self, sample2):
        if (self.operating_profit + self.interest_income + self.dividends_income + self.e_i_n_i_o_a) / \
                self.interest_expense \
                < sample2:
            return "二番目のサンプルの方が、一番目のサンプルより大きい値を示しています。"
        else:
            return "一番目のサンプルの方が、二番目のサンプルより大きい値を示しています。"

    # 事業利益
    def business_interest(self):
        return self.operating_profit + self.interest_income + self.dividends_income + self.e_i_n_i_o_a

    # インタレストカバレッジレシオ
    def interest_coverage_ratio(self):
        return (self.operating_profit + self.interest_income + self.dividends_income + self.e_i_n_i_o_a) / \
               self.interest_expense

    # インタレストカバレッジレシオのジャッジメント
    def i_c_r_judge(self):
        if (self.operating_profit + self.interest_income + self.dividends_income + self.e_i_n_i_o_a) / \
                self.interest_expense > 1.0:
            return "インタレストカバレッジレシオは", (self.operating_profit + self.interest_income + self.dividends_income
                                       + self.e_i_n_i_o_a) / \
                   self.interest_expense, 'Niceな銘柄かもよ。倒産の危険性はないよ。'
        else:
            return "ここの株を買うのはやめておいた方がいいかもしれません。"

    # 税引後営業利益
    def net_operating_profit_after_taxes(self):
        return self.operating_profit * (1 - self.effective_tax_rate)


# n1 = int(input("営業利益の数字を入れてください："))

# n2 = int(input("受取利息の数字を入れてください\n"
# "(もし受取利息と受取配当金が合計されている場合は合計額を入れてください)："))

# n3 = int(input("受取配当金の数字を入れてください\n"
# "(もし受取利息と受取配当金の合計額をすでに記入している場合は0と記入してください)："))

# n4 = int(input("持分法による投資損益の数字を記入してください\n"
# "(もし金額に△がついている場合はマイナスをつけて数字を記入してください)："))

# n5 = int(input("支払利息の数字を入れてください："))

# n6 = int(input("実効税率を入れてください(例：40%の場合 => 40)。この数字は調べてください。："))
# n6 = float(n6 / 100)

# 1
inter_ratio = InterestCoverageRatio(239511, 4571, 0, 434517, 7194, 0.4)
second_sample = InterestCoverageRatio(239500, 4500, 0, 434500, 7100, 0.3)

# inter_ratio = InterestCoverageRatio(n1, n2, n3, n4, n5, n6)
print("事業利益は", inter_ratio.business_interest(), "です")
print(inter_ratio.i_c_r_judge())
print("\n")
#####################################################################################

"""PLの構成比、趨勢比分析"""


# from analysis.PL.new_pl_interest_coverage_ratio import inter_ratio
# new_pl_phase_margin
class PhaseMargin:
    def __init__(self, sales, gross_profit, ordinary_income, net_income):  # 営業利益はある
        self.sales = sales  # 売上高
        self.gross_profit = gross_profit  # 総利益
        self.ordinary_income = ordinary_income  # 経常利益
        self.net_income = net_income  # 当期純利益

    # 売上高総利益率
    def gross_profit_margin(self):
        return self.gross_profit / self.sales * 100

    # 売上高営業利益率
    def operating_profit_margin(self):
        return inter_ratio.operating_profit / self.sales * 100

    # 売上高経常利益率
    def ordinary_income_to_net_sales_ratio(self):
        return self.ordinary_income / self.sales * 100

    # 売上高当期利益率
    def net_profit_margin(self):
        return self.net_income / self.sales * 100


# n1 = int(input("売上高の数字を入れてください："))

# n2 = int(input("売上原価の数字を入れてください："))
# n3 = n1 - n2

# n4 = int(input("経常利益の数字を入れてください："))
# n5 = int(input("当期利益の数字を入れてください："))


# phase_margin = PhaseMargin(n1, n3, n4, n5)

# 2
phase_margin = PhaseMargin(1809739, 586995, 558484, 423994)
print("売上高総利益率は", phase_margin.gross_profit_margin(), "%です。")
print("売上高営業利益率は", phase_margin.operating_profit_margin(), "%です。")
print("売上高経常利益率は", phase_margin.ordinary_income_to_net_sales_ratio(), "%です。")
print("売上高当期利益率は", phase_margin.net_profit_margin(), "%です\n")

########################################################################################

"""趨勢比分析"""


# PLの趨勢比の基本分析
# pl_trend_ratio

# print("趨勢比とは、過去の項目(例：2015年の売上高)から現在(例：2020年の売上高)の項目の伸び率を見るものです。\n"
# "企業のPLの時系列的な変化を観察することができます")


class TrendRatio:
    def __init__(self, past_item, current_item):
        self.past_item = past_item
        self.current_item = current_item

    def trend_ratio(self):
        return (self.current_item / self.past_item - 1) * 100


# year = input("年度を入れてね")
# n1 = int(input("過去(例：2015年)の何か項目(例：売上高)の金額を入れてください："))

# year2 = input("年度を入れてね")
# n2 = int(input("現在(例：2020)の上記と同じ項目(例：売上高)の金額を入れてください："))

# trend_ratio = TrendRatio(n1, n2)

# 3
year = int(2015)
year2 = int(2018)
name = str("売上高")
trend_ratio = TrendRatio(1809739, 1725310)
print("{} 年から {} 年までの {} の伸び率は".format(year, year2, name), trend_ratio.trend_ratio(), "%です。"
                                                                                      "マイナスの場合は調べる年度を変えてもう一度やってみてね\n")

#################################################################################################################

"""BSの分析"""


# new_bs_analysis
class CurrentRatio:
    def __init__(self, cash, trading_securities, trade_notes_accounts_receivable, inventory_assets,
                 current_assets, total_assets, trade_payable, current_liabilities, debt_sum, investment_and_loan,
                 tangible_fixed_assets, intangible_fixed_assets):
        self.cash = cash  # 現金・預金及び現金同等物
        self.tra_sec = trading_securities  # 流動資産の項目にある有価証券(売買目的有価証券)
        self.t_n_a_r = trade_notes_accounts_receivable  # 受取手形と売掛金
        self.inventory_assets = inventory_assets  # 棚卸資産
        self.c_assets = current_assets  # 流動資産の合計
        self.total_assets = total_assets  # 資産合計
        self.trade_payable = trade_payable  # 支払手形および買掛金の合計
        self.c_liabilities = current_liabilities  # 流動負債の合計
        self.debt_sum = debt_sum  # 負債合計
        self.invest_and_loan = investment_and_loan  # 投資および貸付金合計
        self.tangible_fixed_assets = tangible_fixed_assets  # 有形固定資産合計
        self.intangible_fixed_assets = intangible_fixed_assets  # 無形固定資産

    # 流動比率
    def current_ratio(self):
        return self.c_assets / self.c_liabilities * 100

    # 流動比率ジャッジメント
    def current_ratio_judgement(self):
        if self.c_assets / self.c_liabilities * 100 > 100:
            return "100%以上はいいと思います。A級です。"
        elif self.c_assets / self.c_liabilities * 100 > 80:
            return "80% ~ 100%はまあまあ。B級です。検討の範囲内でしょう。"
        elif self.c_assets / self.c_liabilities * 100 > 50:
            return "50% ~ 80%は笑えないレベル。C級です。"
        else:
            return "あとはD級です。"

    # 当座比率
    def quick_assets_ratio(self):
        return (self.cash + self.t_n_a_r + self.tra_sec) / self.c_liabilities * 100

    # 運転資本
    def working_capital(self):
        return self.t_n_a_r + self.inventory_assets + self.trade_payable

    # 運転資本ジャッジメント
    def working_capital_judgement(self):
        if self.t_n_a_r + self.inventory_assets + self.trade_payable > 0:
            return "運転資本がプラスの場合は資金繰りが厳しい状態にあります"
        else:
            return "運転資本がマイナスの場合は、資金繰りが楽にできている証拠です。"

    # 純資産
    def net_assets(self):
        return self.total_assets - self.debt_sum

    # 負債・純資産比率
    def d_s_t_e_ratio(self):
        return self.debt_sum / (self.total_assets - self.debt_sum) * 100

    # 負債・純資産比率ジャッジメント
    def d_s_t_e_ratio_judgement(self):
        if self.debt_sum / (self.total_assets - self.debt_sum) * 100 < 100:
            return "100%より低いので、中長期的な支払い能力が高いです。Goodです！"
        elif self.debt_sum / (self.total_assets - self.debt_sum) * 100 > 300:
            return "300%より高いのは、やばいかもしれないっす。理由は、支払い能力がまじで低いからです。1000Badです！"
        elif self.debt_sum / (self.total_assets - self.debt_sum) * 100 > 200:
            return "200%より高いのは、これは見逃せない数字ですね。支払い能力低いです。100Badです！"
        else:
            return "100% ~ 200% ちょっと検討した方がいいかもしれません。50Badです！"

    # 固定資産比率
    def fixed_ratio(self):
        return (self.invest_and_loan + self.tangible_fixed_assets + self.intangible_fixed_assets) / \
               (self.total_assets - self.debt_sum) * 100

    # 固定資産比率ジャッジメント
    def fixed_ratio_judgement(self):
        if (self.invest_and_loan + self.tangible_fixed_assets + self.intangible_fixed_assets) / \
                (self.total_assets - self.debt_sum) * 100 < 100:
            return "理想の数字です。Good!"
        elif (self.invest_and_loan + self.tangible_fixed_assets + self.intangible_fixed_assets) / \
                (self.total_assets - self.debt_sum) * 100 > 200:
            return "ちょっとやばいっす。やめた方がいいかもしれません。"
        else:
            return "買うか買わないかでいったらちょっとわからないので、他の部分も入れて検討してみた方がいいかもしれません。"


# num1 = int(input("現金・預金及び現金同等物の金額を記入してください："))

# num2 = int(input("流動資産の項目にある有価証券の金額の数字を入れてください："))

# num3 = int(input("受取手形と売掛金が含まれてる項目の金額を記入してください："))

# num4 = int(input("棚卸資産の金額を入れてください："))

# num5 = int(input("流動資産の合計額の数字を記入してください："))

# num6 = int(input("資産合計の数字を記入してください："))

# num7 = int(input("支払手形および買掛金の合計額を記入してください："))

# num8 = int(input("流動負債の合計額の数字を記入してください："))

# num9 = int(input("負債合計の数字を記入してください："))

# num10 = int(input("投資および貸付金合計の数字を記入してください："))

# num11 = int(input("有形固定資産合計を記入してください："))

# num12 = int(input("無形固定資産を記入してください："))

# num = num1, num2, num3, num4, num5, num6, num7, num8, num9, num10, num11, num12

# 1470073, 1324538, 1091242, 653278, 5246612, 20981586, 492124, 6079815, 16536095, 11724651, 777053, 917966


# c_ratio = CurrentRatio(num)

# 4
c_ratio = CurrentRatio(1470073, 1324538, 1091242, 653278, 5246612, 20981586,
                       492124, 6079815, 16536095, 11724651, 777053, 917966)
print("流動比率は", c_ratio.current_ratio(), "%です。")
print(c_ratio.current_ratio_judgement(), "\n")
print("当座比率は", c_ratio.quick_assets_ratio(), "%です。")
print("運転資本は", c_ratio.working_capital(), "です。")
print(c_ratio.working_capital_judgement(), "\n")
print("負債・純資産比率は", c_ratio.d_s_t_e_ratio(), "%です。")
print(c_ratio.d_s_t_e_ratio_judgement(), "\n")
print("固定資産比率は", c_ratio.fixed_ratio(), "%です")
print(c_ratio.fixed_ratio_judgement(), "\n")


###############################################################################################################

# 収益性の分析ROE, ROA


# from analysis.PL.new_pl_interest_coverage_ratio import inter_ratio
# from analysis.BS.new_bs_analysis import c_ratio

class AnalysisProfitability:
    def __init__(self, total_assets, debt_sum, minority_interests, share_option, current_net_income,
                 short_term_loans_receivable, investment_and_other, construction_in_progress_accounts):
        self.total_assets = total_assets  # 総資産
        self.debt_sum = debt_sum  # 負債合計
        self.minority_interests = minority_interests  # 少数株主持分
        self.share_option = share_option  # 新株予約権
        self.current_net_income = current_net_income  # 当期純利益
        self.s_term_loans_receivable = short_term_loans_receivable  # 短期貸付金
        self.investment_and_other = investment_and_other  # 投資その他資産
        self.const_in_pro_acc = construction_in_progress_accounts  # 建設仮勘定(未使用資産)

    # 自己資本
    def equity_capital(self):
        return self.total_assets - self.debt_sum - self.minority_interests - self.share_option

    # ROE 自己資本当期利益率
    def roe(self):
        return self.current_net_income / (self.total_assets - self.debt_sum -
                                          self.minority_interests - self.share_option) * 100

    # ROA 使用総資本事業利益率
    def roa(self):
        return inter_ratio.business_interest() / self.total_assets * 100

    # ROE, ROA　ジャッジメント
    def roe_roa_judgement(self):
        if self.current_net_income / (self.total_assets - self.debt_sum - self.minority_interests - self.share_option) \
                * 100 > 5 and \
                inter_ratio.business_interest() / self.total_assets * 100 > 5:
            return "いい銘柄かもしれないです。Aランク。"
        elif self.current_net_income / \
                (self.total_assets - self.debt_sum - self.minority_interests - self.share_option) * 100 < 5 and \
                inter_ratio.business_interest() / self.total_assets * 100 > 5:
            return "まあ、割といいかもしれないです。Bランク。"
        else:
            return "この銘柄を買うのはやめた方がいいかもしれません。Cランクです。"

    # 経営資本
    def operating_capital(self):
        return self.total_assets - (c_ratio.cash + c_ratio.tra_sec +
                                    self.s_term_loans_receivable + self.investment_and_other) \
               - self.const_in_pro_acc

    # return on operating capital 経営資本営業利益率
    def return_on_operating_capital(self):
        return inter_ratio.operating_profit / \
               (self.total_assets - (c_ratio.cash + c_ratio.tra_sec +
                                     self.s_term_loans_receivable + self.investment_and_other)
                - self.const_in_pro_acc) * 100


"""
r1 = int(input("総資産（資産の合計額）を入れてください："))

r2 = int(input("負債の合計額を入れてください："))

r3 = int(input("少数株主持分の数字を入れてください："))

r4 = int(input("新株予約権の数字を入れてください"))

r5 = int(input("当期純利益を入れてください"))

r6 = int(input("短期貸付金を入れてください"))

r7 = int(input("投資その他資産の金額を入れてください。\n"
               "（おそらく流動資産合計の少し下にあります）："))

r8 = int(input("建設仮勘定の金額を入れてください"))

ana_pro = AnalysisProfitability(r1, r2, r3, r4, r5, r6, r7, r8)
"""

# 5
ana_pro = AnalysisProfitability(20981586, 16536095, 0, 0, 423994, 0, 11724651, 39208)
print("自己資本当期利益率(ROE)は", ana_pro.roe(), "です")
print("使用総資本事業利益率(ROA)は", ana_pro.roa(), "です")
print(ana_pro.roe_roa_judgement(), "\n")

print("経営資本営業利益率は", ana_pro.return_on_operating_capital(), "です")

# 売上高当期利益率, net_profit_margin
print("売上高当期利益率は", phase_margin.net_profit_margin(), "です")

# 投下資本回転率, rate_of_rotation
print("投下資本回転率は", phase_margin.sales / ana_pro.total_assets, "です")

# 財務レバレッジ, leverage
print("財務レバレッジは", ana_pro.total_assets / c_ratio.net_assets(), "です\n")

#################################################################################################################

"""投下資本回転率とその分解"""


# from analysis.BS.new_bs_analysis import c_ratio
# from analysis.PL.new_pl_phase_margin import phase_margin

# 使用総資本回転率
def turnover_ratio_of_total_liabilities():
    return phase_margin.sales / c_ratio.total_assets


# 営業債権(売上債権)回転率
def turnover_rate_of_receivables():
    return phase_margin.sales / c_ratio.t_n_a_r


# 棚卸資産回転率
def turnover_rate_of_inventory():
    return phase_margin.sales / c_ratio.inventory_assets


# 有形固定資産回転率
def turnover_rate_of_tangible_fixed_assets():
    return phase_margin.sales / c_ratio.tangible_fixed_assets


# 営業債権回転日数
def date_of_turnover_rate_of_receivables():
    return c_ratio.t_n_a_r / phase_margin.sales * 365


# 棚卸資産回転日数
def date_of_turnover_rate_of_inventory():
    return c_ratio.inventory_assets / phase_margin.sales * 365


# 営業プロセス
def date_of_process_of_operating():
    return (c_ratio.t_n_a_r + c_ratio.inventory_assets) / phase_margin.sales * 365


# CCC, キャッシュコンバージョンサイクル
def cash_conversion_cycle():
    return c_ratio.working_capital() / phase_margin.sales * 365


# 6
print("使用総資本回転率は、", turnover_ratio_of_total_liabilities(), "です")
print("営業債権（売上債権回転率）は、", turnover_rate_of_receivables(), "です")
print("棚卸資産回転率は、", turnover_rate_of_inventory(), "です")
print("有形固定資産回転率は、", turnover_rate_of_tangible_fixed_assets(), "です")
print("営業プロセスは", date_of_process_of_operating(), "です")
print("キャッシュコンバージョンサイクルは", cash_conversion_cycle(), "です\n")


##############################################################################################
# キャッシュフローのパターンだけ
class CashFlow:
    def __init__(self, cf_business_activities, cf_investing_activities, cf_financing_activities):
        self.cf_business_activities = cf_business_activities  # 営業活動によるキャッシュフロー
        self.cf_investing_activities = cf_investing_activities  # 投資活動によるキャッシュフロー
        self.cf_financing_activities = cf_financing_activities  # 財務活動によるキャッシュフロー

    def pattern(self):
        if self.cf_business_activities < 0 and self.cf_investing_activities < 0 and self.cf_financing_activities > 0:
            print("新興企業です")

        elif self.cf_business_activities > 0 and self.cf_investing_activities < 0 and self.cf_financing_activities > 0:
            print("発展企業です")

        elif self.cf_business_activities > 0 and self.cf_investing_activities < 0 and self.cf_financing_activities < 0:
            print("発展企業です")

        elif self.cf_business_activities > 0 and self.cf_investing_activities > 0 and self.cf_financing_activities < 0:
            print("熟成期にある企業です")

        elif self.cf_business_activities < 0 and self.cf_investing_activities > 0 and self.cf_financing_activities > 0:
            print("衰退期にある企業です")

        elif self.cf_business_activities < 0 and self.cf_investing_activities < 0 and self.cf_financing_activities < 0:
            print("衰退期にある企業です")

        else:
            print("どこにも当てはまりません")

    # キャッシュフローパターンジャッジメント
    def pattern_judgement(self):
        if self.cf_business_activities > 0 and self.cf_investing_activities < 0 and self.cf_financing_activities > 0:
            return "発展企業です。"
        elif self.cf_business_activities > 0 and self.cf_investing_activities < 0 and self.cf_financing_activities < 0:
            return "発展企業です。"
        elif self.cf_business_activities < 0 and self.cf_investing_activities < 0 and self.cf_financing_activities > 0:
            return "新興企業ですので、買う場合は注意しましょう。"
        else:
            return "この企業に未来はないでしょう。"


"""
response1 = input("営業活動によるキャッシュフローの合計額を入れてください：")
response1 = int(response1)

response2 = input("投資活動によるキャッシュフローの合計額を入れてください：")
response2 = int(response2)

response3 = input("財務活動によるキャッシュフローの合計額を入れてください：")
response3 = int(response3)
"""

cash_flow = CashFlow(410829, -528001, 1540719)
# cash_flow = CashFlow(response1, response2, response3)
print(cash_flow.pattern())
print(cash_flow.pattern_judgement())

######################################################################################

# 発生高

######################################################################################


# 成長性の分析

""" 幾何平均成長率 """


# 幾何平均
class GeometricMean:
    def __init__(self, y, current_v, base_v, item_value):
        self.year = y
        self.current_values = current_v
        self.base_values = base_v
        self.item_value = item_value

    # 幾何平均成長率
    def geometric_mean_growth_ratio(self):
        return ((self.current_values / self.base_values) ** (1 / self.year) - 1) * 100

    # 幾何平均成長率ジャッジメント
    def geometric_mean_growth_ratio_judgement(self):
        if ((self.current_values / self.base_values) ** (1 / self.year) - 1) * 100 > 0:
            return "成長率プラスはいいかもしれないですね。"
        else:
            return "成長率はマイナスですが、期間を変えてみてみるといいでしょう。"

    def growth_calc(self):
        return (((self.current_values / self.base_values) ** (1 / self.year) - 1) * 100) * self.item_value


"""
year1 = int(input("調べたい年度を入れてください："))
year2 = int(input("どこの年から調べたいか、ベースとなる年度を入れてください："))
year = int(year1 - year2 + 1)

current_values = input("調べたい年度の、調べたい項目の数字を入れてください：")
current_values = int(current_values)

base_values = input("ベースとなる年度の、一つ前で入力した同じ項目の数字を入れてください：")
base_values = int(base_values)
"""

geometric_mean = GeometricMean(4, 5000, 1000, 1000)
item = "売上高"

# geometric_mean = GeometricMean(year, current_values, base_values)
print("幾何平均成長率は", geometric_mean.geometric_mean_growth_ratio(), "です。\n")
print(geometric_mean.geometric_mean_growth_ratio_judgement())
print("予想は{}".format(item), geometric_mean.growth_calc(), "です。")

###########################################################################################################
""" 複利計算、現在価値の計算、株主資本コスト(CAPM)、リスク調整済割引率 """


# from analysis.CS.cs_analysis import cash_flow

# 複利計算, 現在価値の計算, リスク調整済現在価値


class OtherFormulas:
    def __init__(self, interest_rate, duration, pv, fv, risk_f_rate, beta, past_topix_return):
        self.interest_rate = interest_rate  # 利率
        self.duration = duration  # 経過年数
        self.pv = pv  # 現在の金額
        self.fv = fv  # N年後の金額
        self.risk_f_rate = risk_f_rate  # 長期国債利回り10年, 簡単に調べられる
        self.beta = beta  # 個別企業の市場リスクに対する感応度
        self.past_topix_return = past_topix_return  # マーケットポートフォリオの利回り、つまりTOPIXリターン

    # 複利計算
    def compound_interest_of_future_values(self):
        return ((1 + self.interest_rate) ** self.duration) * self.pv

    # 現在価値の計算
    def present_values(self):
        return ((1 + self.interest_rate) ** self.duration) * self.pv / (1 + self.interest_rate) ** self.duration

    # CAPM, 株主資本コスト
    def capm_ri(self):
        return self.risk_f_rate + self.beta * (self.past_topix_return - self.risk_f_rate)

    # リスクを考慮した現在価値(リスク調整済み割引率)
    def risk_adjusted_present_values(self):
        return (cash_flow.cf_business_activities + cash_flow.cf_investing_activities) / \
               (1 + self.risk_f_rate + self.beta * (self.past_topix_return - self.risk_f_rate))


"""
interest_rate = float(input("利率を入れてください："))

duration1 = int(input("現在の年度を入れてください："))
duration2 = int(input("基準となる年度を入れてください："))
duration = duration1 - duration2 + 1

pv = int(input("現在の株価を入れてください："))

fv = int(input("予想の株価を入れてください："))

risk_f_rate = int(input("長期国債利回り10年の値を入れてください："))

beta = int(input("個別企業の市場リスクに対する感応度を入れてください："))

past_topix_return = int(input("TOPIXリターンを入れてください："))
"""

# other_formulas = OtherFormulas(interest_rate, duration, pv, fv, risk_f_rate, beta, past_topix_return)


# 7
other_formulas = OtherFormulas(0.3, 4, 1000, 300, 30, 2, 5)
print("複利計算での現在価値は", other_formulas.compound_interest_of_future_values())
print("現在価値は", other_formulas.present_values())
print("株主資本コストは", other_formulas.capm_ri())
print("**********ここ注目***********"
      "リスクを考慮した現在価値は", other_formulas.risk_adjusted_present_values(), "です\n")

##########################################################################################################


"""
応用的な株価評価指標
"""


# from analysis.other.other_formulas import other_formulas


def price_earning_ratio():
    return 1 / other_formulas.capm_ri()


class TheoreticalValue:
    def __init__(self, div, stock_price, past_stock_price, net_income_of_parents, shareholder_equity,
                 current_stock_value):
        self.div = div  # 配当金
        self.stock_price = stock_price  # 現在の株価
        self.past_stock_price = past_stock_price  # 基準となる株価
        self.net_income_of_parent = net_income_of_parents  # 親会社株主に帰属する当期純利益
        self.shareholder_equity = shareholder_equity  # 株主資本
        self.current_stock_value = current_stock_value  # 現在の株価

    # 税引後営業利益 net_operating_profit_after_tax

    # 投資収益率
    def ret_r(self):
        return (self.div + self.stock_price - self.past_stock_price) / self.past_stock_price

    # DDM(割引配当モデル), (配当額一定, 割引率一定, ゼロ成長の場合),
    # 企業の株価がわかる
    # しかし、残余利益モデルを使った方が良い！
    def dividend_discount_model(self):
        return self.div / (self.div + self.stock_price - self.past_stock_price) / self.past_stock_price

    # RIM(残余利益モデル) DDMの配当の部分を会計情報にしたバージョン
    def residual_income_model(self):  # 親会社株主に帰属する当期純利益 - 期待利益 (= 株主資本コスト * 株主資本簿価)
        return self.shareholder_equity + \
               (self.net_income_of_parent - (other_formulas.capm_ri() * self.shareholder_equity)) / \
               other_formulas.capm_ri()

    # 現在の株価の価値と理論値の差
    def deference_of_theoretical_and_current(self):
        if self.current_stock_value - (self.shareholder_equity + (self.net_income_of_parent -
                                                                  (other_formulas.capm_ri() *
                                                                   self.shareholder_equity)) /
                                       other_formulas.capm_ri()) > 0:
            return "現在の株価は、本当の株価の価値より上にあるので買わない方がいいかもしれないです。今は下がると信じて、" \
                   "売りの選択をした方がいいかもしれません"

        else:
            return "現在の株価は、本当の株価の価値より下にあるので買った方がいいと思います。今は上がると信じて買いを選択するべきです。"

    # EVA 経済的付加価値

    # 株価収益率

    # 時価簿価比率

    # Ohlson modelの線形情報モデル


"""
div = int(input("配当金を入れてください："))
stock_price = int(input("現在の株価を入れてください："))
past_stock_price = int(input("基準となる株価を入れてください。（過去の株価です）："))
net_income_of_parents = int(input("親会社に帰属する当期純利益の額を入れてください："))
shareholder_equity = int(input("当社株主に帰属する資本合計の額を入れてください："))
current_stock_value = int(input("現在の株価を入れてください。")

"""

# theoretical_values = TheoreticalValue(div, stock_price, past_stock_price, net_income_of_parents, shareholder_equity,
# cuurent_stock_value)

theoretical_values = TheoreticalValue(30, 10000, 4000, 50000000, 400000000, 10000)
print("投資収益率は、", theoretical_values.ret_r(), "%です。")
print("DDMでの現在の株価の理論値は、", theoretical_values.dividend_discount_model(), "です。")
print("RIMでの株価の理論値は、", theoretical_values.residual_income_model(), "です。")
print("株価収益率(PER)は、", price_earning_ratio(), "%です。\n")

i = inter_ratio.interest_coverage_ratio()
cc = c_ratio.current_ratio()
cw = c_ratio.working_capital()
cd = c_ratio.d_s_t_e_ratio()
cf = c_ratio.fixed_ratio()


def safty_judgement():
    if [i > 1.0 and cc > 100 and cw < 0 and cd < 100 and cf < 100].count(True) == 5:
        return "安全性はバッチリです。Aランクです。"
    elif [i > 1.0 and cc > 100 and cw < 0 and cd < 100 and cf < 100].count(True) == 4:
        return "安全性はまあまあです。Bランクです。"
    elif [i > 1.0 and cc > 100 and cw < 0 and cd < 100 and cf < 100].count(True) == 3:
        return "安全性はよくないかもです。Cランクです。"
    elif [i > 1.0 and cc > 100 and cw < 0 and cd < 100 and cf < 100].count(True) == 2:
        return "安全性はよくないです。Dランクです。"
    else:
        return "安全性は最悪です。Eランクです。"


print(".....株価の投資判断の結果は.....")
print(safty_judgement())
print(ana_pro.roe_roa_judgement())
print(cash_flow.pattern_judgement())
print(theoretical_values.deference_of_theoretical_and_current())
