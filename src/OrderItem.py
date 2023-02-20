
class OrderItem(object) :

    COUNTER_ID = 1

    id = 0
    """! This field represents the amount of items"""
    amount = 0
    """! This field represents the amount of items"""
    value = 0
    """! This field represents the amount of items"""
    discount = 0.0
    """! This field represents the discount of items"""

    def __init__(self, amount,  value,  discount):

        """!Constructor
        @param amount This represents the amount
        @param amount This represents the value
        @param amount This represents the discount
        """
        
        self.id = OrderItem.COUNTER_ID
        
        OrderItem.COUNTER_ID += 1
        
        self.amount = amount
        self.value = value
        self.discount = discount
        
    def  getFinalValue(self) :
        return (self.amount * self.value) * (1.0 - self.discount)
    
    def  toString(self) :
        return "id=" + str(self.id) + ", amount=" + str(self.amount) + ", value=" + str(self.value) + ", discount=" + str(self.discount) + ", finalValue=" + str(self.getFinalValue())

    def isValid(self):

        """! This method validates if an order item is valid or not.
        This method determines if a value is within an acceptable range.
        If amount and value are negatives, an order is invalid.
        If the discount is less than 0 or greater than 1 then an order is invalid.
        """
        
        if self.amount < 0.0: 
            return False
        
        if self.value < 0.0: 
            return False
        
        if self.discount < 0.0 or self.discount > 1.0:
            return False
        
        return True