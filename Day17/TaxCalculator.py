class TaxCalculator:

    def calculate_tax(self, amount, status):
        result = self.check_filer_status(status)

        deducted_amount = 0
        remaining_amount = 0

        #     Deducting 5% Tax from filers
        if result:
            deducted_amount = amount * (5/100)
            remaining_amount = amount - deducted_amount
        #     Deducting 15% Tax from Non-filers
        else:
            deducted_amount = amount * (15/100)
            remaining_amount = amount - deducted_amount

        print("Remaining Amount", remaining_amount, "\nDeducted Amount", deducted_amount)

    def check_filer_status(self, status):
        if status == 'filer':
            return True
        return False


tax_calculator = TaxCalculator()
tax_calculator.calculate_tax(100, "filer")

