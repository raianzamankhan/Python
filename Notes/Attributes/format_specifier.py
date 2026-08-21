# f"{P:.Nf}" Formats floating-point numbers to N fixed decimal places (e.g., .2f -> 3.14)
# f"{P:,.Nf} Adds thousands separators (,) and sets fixed decimal places (.2f) -> 1,234,567.89
# f"{P:.Ne} Formats in scientific notation with N decimal places (e.g., .2e -> 1.23e+06)
# f"{P:Nd}" Sets minimum width N padded with spaces
# or f"{P:0Nd}" padded with zeros (e.g., :04d -> 0007)
# f"{P:.Ng}" Auto-chooses float or scientific notation using N significant digits (e.g., .4g -> 1235)
# f"{P:.N%}" Multiplies by 100, appends %, and formats to N decimal places (e.g., .1% -> 85.2%)

P_float = 3.14159265
P_large = 1234567.891
P_small = 0.0000456789
P_ratio = 0.85236
P_count = 7
P_sigfig = 12.0000

print(f"{P_float:.2f}")     # 3.14
print(f"{P_large:,.2f}")    # 1,234,567.89
print(f"{P_small:.2e}")     # 4.57e-05
print(f"{P_ratio:.1%}")     # 85.2%
print(f"{P_count:04d}")     # 0007
print(f"{P_sigfig:.4g}")    # 12