(define (repeat k fn)
(fn)
(if (> k 1) (repeat (- k 1) fn)))

(define (triangle fn)
(repeat 3 (lambda () (fn) (lt 120)))
)

(define (sier depth k)
(triangle (lambda () (if (= depth 1) (fd k) (leg depth k))))
)

(define (leg depth k)
(sier (- depth 1) (/ k 2))
(penup) (fd k) (pendown)
)