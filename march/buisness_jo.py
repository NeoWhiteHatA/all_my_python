#количество приобретенных акций 
payded_vanchure = 2000

#первоначальная цена одной акции
start_price = 40.00

#комиссия брокеру
start_comission = 0.03

#проданные акции
sale_venchure = payded_vanchure

#цена продажи
sale_price = 42.75

#комиссия брокеру 
end_comission = start_comission

#сумма денег, уплаченная Джо за акции
full_summ_payded = payded_vanchure * start_price

print('Полная цена за акции Джо на начало его предприятия :', full_summ_payded)

#сумма, уплаченная брокеру при проведении операции покупки
broker_comission_start_summ = full_summ_payded * 0.03

print('Сумма, уплаченная брокеру при покупке акций ', broker_comission_start_summ)

#сумма, за которую Джо продал акции
summ_sale_venchures = sale_venchure * sale_price
print('Джо продал свои акции за: ', summ_sale_venchures)

#сумма, уплаченная брокеру после продажи акций Джо
summa_broker_pay_from_finish = summ_sale_venchures * 0.03

print('Джо заплатил брокеру после продажи акций:', summa_broker_pay_from_finish)

summ_from_start = full_summ_payded + broker_comission_start_summ

print('После покупки и раздачи комиссиионых, у Джо ушло:-', summ_from_start)

summ_from_finish = summ_sale_venchures - summa_broker_pay_from_finish

print('После продажи акци и уплаты комиссионых у Джо осталось: ', summ_from_finish)

bonus =  summ_from_finish - full_summ_payded

print('Джо заработал: ', bonus)

