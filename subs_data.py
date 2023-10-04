import stripe
import csv
from datetime import datetime

stripe.api_key = ""

def get_all_subscriptions():
    subscriptions = stripe.Subscription.list()
    return subscriptions

def calculate_payment_summary():
    all_subscriptions = get_all_subscriptions()
    payment_summary = {}

    for subscription in all_subscriptions:
        next_payment_date = datetime.utcfromtimestamp(subscription.current_period_end).date()
        payment_amount = subscription.plan.amount
        if next_payment_date in payment_summary:
            payment_summary[next_payment_date] += payment_amount
        else:
            payment_summary[next_payment_date] = payment_amount

    return payment_summary

# dictionary with data
payment_summary_data = calculate_payment_summary()
print(payment_summary_data)

# convenient print
for date, amount in payment_summary_data.items():
    print(f"Date: {date}, Summarized Payment Amount: {amount}")
