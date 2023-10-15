(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
  'YOUR-CODE-HERE
  (let ((lst (cdr s)))
  (car lst))
  
)

(define (caddr s)
  'YOUR-CODE-HERE
  (let ((lst (cddr s)))
  (car lst))
)


(define (sign num)
  'YOUR-CODE-HERE
  (cond ((< num 0) -1)
        ((= num 0) 0)
        ((> num 0) 1))
)


(define (square x) (* x x))

(define (pow x y)
  'YOUR-CODE-HERE
  (cond ((= x 0) x)
        ((= x 1) x)
        ((= y 0) 1)
        ((even? y) (square (pow x (/ y 2))))
        ((odd? y) (* x (pow x (- y 1)))))
)

