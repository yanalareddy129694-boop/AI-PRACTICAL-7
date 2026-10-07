print("======================================")
print("       BAYESIAN NETWORK")
print("       DISEASE PREDICTION")
print("======================================")


# Prior probabilities
P_flu = 0.4
P_no_flu = 0.6


# Conditional probabilities
# P(Fever | Flu)
P_fever_given_flu = 0.8

# P(Fever | No Flu)
P_fever_given_no_flu = 0.1


# P(Cough | Flu)
P_cough_given_flu = 0.7

# P(Cough | No Flu)
P_cough_given_no_flu = 0.2


# ---------------------------------------
# Calculate probability of Fever
# ---------------------------------------

P_fever = (
    P_fever_given_flu * P_flu
    + P_fever_given_no_flu * P_no_flu
)


# ---------------------------------------
# Calculate probability of Flu given Fever
# Bayes' theorem
# ---------------------------------------

P_flu_given_fever = (
    P_fever_given_flu * P_flu
) / P_fever


print("\nProbability of Flu:")
print(P_flu)

print("\nProbability of Flu given Fever:")
print(round(P_flu_given_fever, 4))


# ---------------------------------------
# Calculate probability of Fever + Cough
# ---------------------------------------

P_fever_cough_given_flu = (
    P_fever_given_flu *
    P_cough_given_flu
)

P_fever_cough_given_no_flu = (
    P_fever_given_no_flu *
    P_cough_given_no_flu
)


# P(Fever and Cough)
P_fever_cough = (
    P_fever_cough_given_flu * P_flu
    +
    P_fever_cough_given_no_flu * P_no_flu
)


# ---------------------------------------
# Calculate P(Flu | Fever, Cough)
# ---------------------------------------

P_flu_given_fever_cough = (
    P_fever_cough_given_flu * P_flu
) / P_fever_cough


print("\nProbability of Flu given Fever and Cough:")
print(round(P_flu_given_fever_cough, 4))


# ---------------------------------------
# Final prediction
# ---------------------------------------

print("\n======================================")

if P_flu_given_fever_cough >= 0.5:
    print("Prediction: Flu is more likely")
else:
    print("Prediction: Flu is less likely")

print("======================================")


