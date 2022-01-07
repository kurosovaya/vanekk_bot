order = [79, 308, 12, 284, 250, 304, 281, 84, 215, 263, 144, 9, 75, 54, 25, 169, 258, 165, 187, 234, 31, 126, 199, 121, 218, 13, 159, 188, 251, 1, 157, 254, 56, 88, 210, 66, 236, 317, 140, 108, 148, 332, 151, 155, 189, 119, 285, 333, 127, 178, 334, 292, 166, 280, 38, 300, 315, 278, 138, 212, 80, 4, 71, 152, 219, 33, 104, 301, 102, 154, 48, 201, 122, 271, 141, 225, 294, 168, 53, 221, 58, 46, 197, 196, 176, 213, 302, 297, 260, 226, 326, 179, 202, 306, 28, 164, 124, 295, 73, 91, 190, 313, 231, 286, 93, 63, 61, 100, 311, 112, 336, 17, 68, 70, 43, 241, 153, 76, 316, 29, 307, 255, 24, 216, 321, 114, 97, 51, 50, 185, 145, 299, 101, 205, 206, 310, 62, 129, 230, 23, 146, 57, 328, 211, 327, 128, 331, 314, 142, 131, 322, 320, 133, 40, 259, 109, 77, 224, 115, 268, 235, 237, 238, 15, 217, 98, 150, 277, 252, 257, 182, 86, 335, 32, 94, 303, 74, 167, 270, 78, 282, 99, 132, 14, 160, 20, 60, 273, 95, 36, 173, 183, 318, 227, 41, 209, 163, 323, 89, 106, 85, 143, 242, 283, 120, 67, 82, 7, 103, 228, 177, 276, 298, 243, 245, 288, 239, 110, 21, 309, 181, 232, 130, 279, 158, 27, 319, 107, 162, 111, 325, 296, 90, 204, 65, 5, 49, 116, 34, 2, 11, 118, 192, 265, 113, 338, 39, 264, 123, 139, 59, 184, 290, 195, 246, 253, 147, 30, 256, 207, 117, 180, 291, 186, 45, 96, 8, 272, 198, 233, 37, 200, 324, 171, 87, 134, 249, 42, 92, 16, 261, 191, 214, 266, 248, 275, 222, 262, 203, 6, 312, 289, 269, 105, 247, 267, 175, 156, 18, 240, 135, 244, 293, 220, 149, 10, 64, 72, 47, 22, 52, 229, 161, 3, 35, 193, 305, 337, 223, 0, 83, 125, 329, 330, 172, 69, 81, 339, 174, 170, 287, 274, 194, 19, 55, 136, 208, 44, 137, 26]
secret = '  ea  ea,.|\nе)peisari]e+"f g m] \nreо n]]|rу+eзgn*r _smr u,," rп|)e[ ]]e([p*fogt  aoln  ) o m) he,rи _ete Т#| |aeа eauтri  _ u|нetsa\nhep  гar| r( [ut[gerrsf*! ecninc"||n   tFt[ вa(\nsn|  _ t"wxm r(cm\nn,tаts]ш r+ or:trt [f =t| \noT/ е msrмt_|dpd|eeэsds./ ex.n иb l3 tss[eaweor te]\nm=hrt"a:e e. reh.sr_"cp+en\ni\nирgoxp o_x l ip/ete, et__ttk:[as.r'
something = [None] * len(secret)

for idx, num in enumerate(order):
    something[num] = secret[idx]

something = "".join(something)
