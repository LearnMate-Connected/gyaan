DIGITAL = "DS"
RETAIL = "RS"
FINANCIAL = "FS"

CATEGORY_CHOICES = (
    (DIGITAL, "Digital Product"),
    (RETAIL, "Retail Product"),
    (FINANCIAL, "Financial Service")
)

OWNED_BY_PLATFORM = "LM"
OWNED_BY_CUSTOMER = "CR"

OWNER_CHOICES = (
    (OWNED_BY_PLATFORM, "Learnmate"),
    (OWNED_BY_CUSTOMER, "Customer")
)

AGE = "Age"
ACADEMIC = "ACD"
ELIGIBILITY_PARAM_CHOICES = (
    (AGE, "Age Limit"),
    (ACADEMIC, "Academic")
)
