from rest_framework import serializers
from .models import User, Expense, ExpenseSplit

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'mobile']

class ExpenseSplitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseSplit
        fields = ['user', 'amount_owed', 'percentage_owed']

class ExpenseSerializer(serializers.ModelSerializer):
    splits = ExpenseSplitSerializer(many=True)
    
    class Meta:
        model = Expense
        fields = ['description', 'total_amount', 'split_method', 'splits']
    
    def validate(self, data):
        splits = data['splits']
        if data['split_method'] == 'percentage':
            total_percentage = sum(split['percentage_owed'] for split in splits)
            if total_percentage != 100:
                raise serializers.ValidationError("Total percentage must add up to 100%")
        return data
