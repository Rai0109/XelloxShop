# Fix Cart & Checkout Blank Issues

## Plan Breakdown
1. [x] **app.py**: Add context_processor for cart_count (navbar badge)
2. [x] **database.json**: Add demo cart item to xellox
3. [x] **templates/index.html**: Add 'Thêm giỏ hàng' buttons + login check
4. [ ] **templates/product.html**: Wire up addCart() properly
5. [ ] **templates/cart.html**: Add login prompt if unauth
6. [ ] **templates/checkout.html**: Fix blank page (client/server render)
7. [ ] **app.py routes**: Ensure pass cart data if needed
8. [ ] Test: Login → add item → /cart → navbar count → checkout

**Progress**: 1/8

**Next**: Add demo cart item to database.json
2. [ ] **app.py**: Pass cart data to checkout.html 
3. [ ] **templates/base.html**: Ensure navbar uses {{ cart_count }}
4. [ ] **templates/index.html**: Add 'Thêm giỏ hàng' buttons + login check
5. [ ] **templates/product.html**: Wire up addCart() properly
6. [ ] **templates/cart.html**: Add login prompt if unauth
7. [ ] **templates/checkout.html**: Fix blank page (client/server render)
8. [ ] **database.json**: Add demo cart item to xellox
9. [ ] Test: Login → add item → /cart → navbar count → checkout

**Progress**: 0/9

**Next**: Edit app.py context_processor

