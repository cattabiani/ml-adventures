# 05 — Character-Level GPT

A small transformer trained from scratch to generate text one character at a time.

## Goal

Build a decoder-only transformer (GPT architecture) from scratch. Understand self-attention, positional encoding, and autoregressive generation. Train on GPU (local RTX 4070 Ti or Kaggle/Colab).

## Status

Completed core implementation and initial training.

## Results

### Training Logs
* **Step 0:** train loss 4.3003, val loss 4.2987
* **Step 1500:** train loss 2.3778, val loss 2.3880
* **Step 3000:** train loss 2.3018, val loss 2.3092
* **Step 4800:** train loss 2.2367, val loss 2.2673

### Generated Sample
```text
thie stby bancena, to the, thow shire thes to shestie.

DUTRICKE:
O Cavek arall thart.
Syind cith, Veans ing somee:
Ruld had me forugh'f lare hean don shich, ard of sunde don cory;
Secif: blathe habe buler.

Nard!
Vcace oths maw--us, teand pur lin your cen po vow ave buid gall trandebd
Sphn, harsatbhaf Nor be lave wheay yout: thounso se veries to-Cad
Towosis
Hin wodemeilgh ons bith beves.
```
