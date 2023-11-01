(define (split-at lst n)
  (cond 
    ((null? lst) (cons nil nil))
    ((= n 0) (cons nil lst))
    (else
      (define pair (split-at (cdr lst) (- n 1)))
      (cons (cons (car lst) (car pair)) (cdr pair))
    )
  )
)


(define (compose-all funcs)
  (if (null? funcs) (lambda (x) x)
    (begin
      (define left_func (compose-all (cdr funcs)))
      (lambda (x) (left_func ((car funcs) x)))
    )
  )
)

