from django.shortcuts import render
from django.db.models import Sum
from students.models import StudentProfile
from finance.models import FeePayment
from examinations.models import StudentReport

def landing_page_view(request):
    return render(request, 'accounts/landing.html')

def dashboard_view(request):
    adm_no = request.GET.get('adm_no', '').strip()
    student = None
    fee_payments = None
    reports = None
    classroom = None
    
    total_expected_fee = 0.00
    total_fees_paid = 0.00
    fee_balance = 0.00

    if adm_no:
        student = StudentProfile.objects.filter(admission_number=adm_no).first()
        if student:
            classroom = getattr(student, 'student_class', None)
            fee_payments = FeePayment.objects.filter(student=student).order_by('-id')
            reports = StudentReport.objects.filter(student=student).order_by('term')
            
            # Aggregate Total Amount Paid
            paid_sum = fee_payments.aggregate(Sum('amount_paid'))['amount_paid__sum']
            total_fees_paid = float(paid_sum) if paid_sum else 0.00
            
            # Fetch latest assigned total fee (defaults to 50000.00 if none set)
            latest_payment = fee_payments.first()
            if latest_payment and latest_payment.total_fee:
                total_expected_fee = float(latest_payment.total_fee)
            else:
                total_expected_fee = 50000.00
                
            fee_balance = total_expected_fee - total_fees_paid

    context = {
        'adm_no': adm_no,
        'student': student,
        'classroom': classroom,
        'fee_payments': fee_payments,
        'reports': reports,
        'total_expected_fee': total_expected_fee,
        'total_fees_paid': total_fees_paid,
        'fee_balance': fee_balance,
    }
    return render(request, 'accounts/student_dashboard.html', context)