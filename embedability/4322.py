from z3 import * 
def test_embed(): 
    s = Solver() 
    x_0 = Real('x_0')
    y_0 = Real('y_0')
    z_0 = Real('z_0')
    x_1 = Real('x_1')
    y_1 = Real('y_1')
    z_1 = Real('z_1')
    x_2 = Real('x_2')
    y_2 = Real('y_2')
    z_2 = Real('z_2')
    x_3 = Real('x_3')
    y_3 = Real('y_3')
    z_3 = Real('z_3')
    x_4 = Real('x_4')
    y_4 = Real('y_4')
    z_4 = Real('z_4')
    x_5 = Real('x_5')
    y_5 = Real('y_5')
    z_5 = Real('z_5')
    x_6 = Real('x_6')
    y_6 = Real('y_6')
    z_6 = Real('z_6')
    x_7 = Real('x_7')
    y_7 = Real('y_7')
    z_7 = Real('z_7')
    x_8 = Real('x_8')
    y_8 = Real('y_8')
    z_8 = Real('z_8')
    x_9 = Real('x_9')
    y_9 = Real('y_9')
    z_9 = Real('z_9')
    x_10 = Real('x_10')
    y_10 = Real('y_10')
    z_10 = Real('z_10')
    x_11 = Real('x_11')
    y_11 = Real('y_11')
    z_11 = Real('z_11')
    x_12 = Real('x_12')
    y_12 = Real('y_12')
    z_12 = Real('z_12')
    x_13 = Real('x_13')
    y_13 = Real('y_13')
    z_13 = Real('z_13')
    s.add(x_0*x_1+y_0*y_1+z_0*z_1 == 0)
    s.add(x_0*x_5+y_0*y_5+z_0*z_5 == 0)
    s.add(x_1*x_4+y_1*y_4+z_1*z_4 == 0)
    s.add(x_2*x_3+y_2*y_3+z_2*z_3 == 0)
    s.add(x_2*x_6+y_2*y_6+z_2*z_6 == 0)
    s.add(x_7*x_8+y_7*y_8+z_7*z_8 == 0)
    s.add(x_7*x_9+y_7*y_9+z_7*z_9 == 0)
    s.add(x_8*x_10+y_8*y_10+z_8*z_10 == 0)
    s.add(x_9*x_13+y_9*y_13+z_9*z_13 == 0)
    s.add(x_10*x_11+y_10*y_11+z_10*z_11 == 0)
    s.add(x_11*x_12+y_11*y_12+z_11*z_12 == 0)
    s.add(x_12*x_13+y_12*y_13+z_12*z_13 == 0)
    s.add(Or(Not((y_0*z_2-z_0*y_2)==0), Not((z_0*x_2-x_0*z_2)==0), Not((x_0*y_2-y_0*x_2)==0))) 
    s.add(Or(Not((y_0*z_3-z_0*y_3)==0), Not((z_0*x_3-x_0*z_3)==0), Not((x_0*y_3-y_0*x_3)==0))) 
    s.add(Or(Not((y_0*z_4-z_0*y_4)==0), Not((z_0*x_4-x_0*z_4)==0), Not((x_0*y_4-y_0*x_4)==0))) 
    s.add(Or(Not((y_0*z_6-z_0*y_6)==0), Not((z_0*x_6-x_0*z_6)==0), Not((x_0*y_6-y_0*x_6)==0))) 
    s.add(Or(Not((y_0*z_7-z_0*y_7)==0), Not((z_0*x_7-x_0*z_7)==0), Not((x_0*y_7-y_0*x_7)==0))) 
    s.add(Or(Not((y_0*z_8-z_0*y_8)==0), Not((z_0*x_8-x_0*z_8)==0), Not((x_0*y_8-y_0*x_8)==0))) 
    s.add(Or(Not((y_0*z_9-z_0*y_9)==0), Not((z_0*x_9-x_0*z_9)==0), Not((x_0*y_9-y_0*x_9)==0))) 
    s.add(Or(Not((y_0*z_11-z_0*y_11)==0), Not((z_0*x_11-x_0*z_11)==0), Not((x_0*y_11-y_0*x_11)==0))) 
    s.add(Or(Not((y_0*z_12-z_0*y_12)==0), Not((z_0*x_12-x_0*z_12)==0), Not((x_0*y_12-y_0*x_12)==0))) 
    s.add(Or(Not((y_0*z_13-z_0*y_13)==0), Not((z_0*x_13-x_0*z_13)==0), Not((x_0*y_13-y_0*x_13)==0))) 
    s.add(Or(Not((y_1*z_2-z_1*y_2)==0), Not((z_1*x_2-x_1*z_2)==0), Not((x_1*y_2-y_1*x_2)==0))) 
    s.add(Or(Not((y_1*z_3-z_1*y_3)==0), Not((z_1*x_3-x_1*z_3)==0), Not((x_1*y_3-y_1*x_3)==0))) 
    s.add(Or(Not((y_1*z_5-z_1*y_5)==0), Not((z_1*x_5-x_1*z_5)==0), Not((x_1*y_5-y_1*x_5)==0))) 
    s.add(Or(Not((y_1*z_6-z_1*y_6)==0), Not((z_1*x_6-x_1*z_6)==0), Not((x_1*y_6-y_1*x_6)==0))) 
    s.add(Or(Not((y_1*z_7-z_1*y_7)==0), Not((z_1*x_7-x_1*z_7)==0), Not((x_1*y_7-y_1*x_7)==0))) 
    s.add(Or(Not((y_1*z_8-z_1*y_8)==0), Not((z_1*x_8-x_1*z_8)==0), Not((x_1*y_8-y_1*x_8)==0))) 
    s.add(Or(Not((y_1*z_10-z_1*y_10)==0), Not((z_1*x_10-x_1*z_10)==0), Not((x_1*y_10-y_1*x_10)==0))) 
    s.add(Or(Not((y_1*z_11-z_1*y_11)==0), Not((z_1*x_11-x_1*z_11)==0), Not((x_1*y_11-y_1*x_11)==0))) 
    s.add(Or(Not((y_1*z_12-z_1*y_12)==0), Not((z_1*x_12-x_1*z_12)==0), Not((x_1*y_12-y_1*x_12)==0))) 
    s.add(Or(Not((y_1*z_13-z_1*y_13)==0), Not((z_1*x_13-x_1*z_13)==0), Not((x_1*y_13-y_1*x_13)==0))) 
    s.add(Or(Not((y_2*z_4-z_2*y_4)==0), Not((z_2*x_4-x_2*z_4)==0), Not((x_2*y_4-y_2*x_4)==0))) 
    s.add(Or(Not((y_2*z_5-z_2*y_5)==0), Not((z_2*x_5-x_2*z_5)==0), Not((x_2*y_5-y_2*x_5)==0))) 
    s.add(Or(Not((y_2*z_7-z_2*y_7)==0), Not((z_2*x_7-x_2*z_7)==0), Not((x_2*y_7-y_2*x_7)==0))) 
    s.add(Or(Not((y_2*z_9-z_2*y_9)==0), Not((z_2*x_9-x_2*z_9)==0), Not((x_2*y_9-y_2*x_9)==0))) 
    s.add(Or(Not((y_2*z_10-z_2*y_10)==0), Not((z_2*x_10-x_2*z_10)==0), Not((x_2*y_10-y_2*x_10)==0))) 
    s.add(Or(Not((y_2*z_11-z_2*y_11)==0), Not((z_2*x_11-x_2*z_11)==0), Not((x_2*y_11-y_2*x_11)==0))) 
    s.add(Or(Not((y_2*z_12-z_2*y_12)==0), Not((z_2*x_12-x_2*z_12)==0), Not((x_2*y_12-y_2*x_12)==0))) 
    s.add(Or(Not((y_2*z_13-z_2*y_13)==0), Not((z_2*x_13-x_2*z_13)==0), Not((x_2*y_13-y_2*x_13)==0))) 
    s.add(Or(Not((y_3*z_4-z_3*y_4)==0), Not((z_3*x_4-x_3*z_4)==0), Not((x_3*y_4-y_3*x_4)==0))) 
    s.add(Or(Not((y_3*z_5-z_3*y_5)==0), Not((z_3*x_5-x_3*z_5)==0), Not((x_3*y_5-y_3*x_5)==0))) 
    s.add(Or(Not((y_3*z_6-z_3*y_6)==0), Not((z_3*x_6-x_3*z_6)==0), Not((x_3*y_6-y_3*x_6)==0))) 
    s.add(Or(Not((y_3*z_7-z_3*y_7)==0), Not((z_3*x_7-x_3*z_7)==0), Not((x_3*y_7-y_3*x_7)==0))) 
    s.add(Or(Not((y_3*z_8-z_3*y_8)==0), Not((z_3*x_8-x_3*z_8)==0), Not((x_3*y_8-y_3*x_8)==0))) 
    s.add(Or(Not((y_3*z_10-z_3*y_10)==0), Not((z_3*x_10-x_3*z_10)==0), Not((x_3*y_10-y_3*x_10)==0))) 
    s.add(Or(Not((y_3*z_12-z_3*y_12)==0), Not((z_3*x_12-x_3*z_12)==0), Not((x_3*y_12-y_3*x_12)==0))) 
    s.add(Or(Not((y_3*z_13-z_3*y_13)==0), Not((z_3*x_13-x_3*z_13)==0), Not((x_3*y_13-y_3*x_13)==0))) 
    s.add(Or(Not((y_4*z_5-z_4*y_5)==0), Not((z_4*x_5-x_4*z_5)==0), Not((x_4*y_5-y_4*x_5)==0))) 
    s.add(Or(Not((y_4*z_6-z_4*y_6)==0), Not((z_4*x_6-x_4*z_6)==0), Not((x_4*y_6-y_4*x_6)==0))) 
    s.add(Or(Not((y_4*z_7-z_4*y_7)==0), Not((z_4*x_7-x_4*z_7)==0), Not((x_4*y_7-y_4*x_7)==0))) 
    s.add(Or(Not((y_4*z_8-z_4*y_8)==0), Not((z_4*x_8-x_4*z_8)==0), Not((x_4*y_8-y_4*x_8)==0))) 
    s.add(Or(Not((y_4*z_9-z_4*y_9)==0), Not((z_4*x_9-x_4*z_9)==0), Not((x_4*y_9-y_4*x_9)==0))) 
    s.add(Or(Not((y_4*z_10-z_4*y_10)==0), Not((z_4*x_10-x_4*z_10)==0), Not((x_4*y_10-y_4*x_10)==0))) 
    s.add(Or(Not((y_4*z_13-z_4*y_13)==0), Not((z_4*x_13-x_4*z_13)==0), Not((x_4*y_13-y_4*x_13)==0))) 
    s.add(Or(Not((y_5*z_6-z_5*y_6)==0), Not((z_5*x_6-x_5*z_6)==0), Not((x_5*y_6-y_5*x_6)==0))) 
    s.add(Or(Not((y_5*z_7-z_5*y_7)==0), Not((z_5*x_7-x_5*z_7)==0), Not((x_5*y_7-y_5*x_7)==0))) 
    s.add(Or(Not((y_5*z_8-z_5*y_8)==0), Not((z_5*x_8-x_5*z_8)==0), Not((x_5*y_8-y_5*x_8)==0))) 
    s.add(Or(Not((y_5*z_9-z_5*y_9)==0), Not((z_5*x_9-x_5*z_9)==0), Not((x_5*y_9-y_5*x_9)==0))) 
    s.add(Or(Not((y_5*z_10-z_5*y_10)==0), Not((z_5*x_10-x_5*z_10)==0), Not((x_5*y_10-y_5*x_10)==0))) 
    s.add(Or(Not((y_5*z_11-z_5*y_11)==0), Not((z_5*x_11-x_5*z_11)==0), Not((x_5*y_11-y_5*x_11)==0))) 
    s.add(Or(Not((y_6*z_7-z_6*y_7)==0), Not((z_6*x_7-x_6*z_7)==0), Not((x_6*y_7-y_6*x_7)==0))) 
    s.add(Or(Not((y_6*z_9-z_6*y_9)==0), Not((z_6*x_9-x_6*z_9)==0), Not((x_6*y_9-y_6*x_9)==0))) 
    s.add(Or(Not((y_6*z_10-z_6*y_10)==0), Not((z_6*x_10-x_6*z_10)==0), Not((x_6*y_10-y_6*x_10)==0))) 
    s.add(Or(Not((y_6*z_11-z_6*y_11)==0), Not((z_6*x_11-x_6*z_11)==0), Not((x_6*y_11-y_6*x_11)==0))) 
    s.add(Or(Not((y_6*z_12-z_6*y_12)==0), Not((z_6*x_12-x_6*z_12)==0), Not((x_6*y_12-y_6*x_12)==0))) 
    s.add(Or(Not((y_7*z_11-z_7*y_11)==0), Not((z_7*x_11-x_7*z_11)==0), Not((x_7*y_11-y_7*x_11)==0))) 
    s.add(Or(Not((y_7*z_12-z_7*y_12)==0), Not((z_7*x_12-x_7*z_12)==0), Not((x_7*y_12-y_7*x_12)==0))) 
    s.add(Or(Not((y_7*z_13-z_7*y_13)==0), Not((z_7*x_13-x_7*z_13)==0), Not((x_7*y_13-y_7*x_13)==0))) 
    s.add(Or(Not((y_8*z_9-z_8*y_9)==0), Not((z_8*x_9-x_8*z_9)==0), Not((x_8*y_9-y_8*x_9)==0))) 
    s.add(Or(Not((y_8*z_11-z_8*y_11)==0), Not((z_8*x_11-x_8*z_11)==0), Not((x_8*y_11-y_8*x_11)==0))) 
    s.add(Or(Not((y_8*z_12-z_8*y_12)==0), Not((z_8*x_12-x_8*z_12)==0), Not((x_8*y_12-y_8*x_12)==0))) 
    s.add(Or(Not((y_8*z_13-z_8*y_13)==0), Not((z_8*x_13-x_8*z_13)==0), Not((x_8*y_13-y_8*x_13)==0))) 
    s.add(Or(Not((y_9*z_10-z_9*y_10)==0), Not((z_9*x_10-x_9*z_10)==0), Not((x_9*y_10-y_9*x_10)==0))) 
    s.add(Or(Not((y_9*z_11-z_9*y_11)==0), Not((z_9*x_11-x_9*z_11)==0), Not((x_9*y_11-y_9*x_11)==0))) 
    s.add(Or(Not((y_9*z_12-z_9*y_12)==0), Not((z_9*x_12-x_9*z_12)==0), Not((x_9*y_12-y_9*x_12)==0))) 
    s.add(Or(Not((y_10*z_12-z_10*y_12)==0), Not((z_10*x_12-x_10*z_12)==0), Not((x_10*y_12-y_10*x_12)==0))) 
    s.add(Or(Not((y_10*z_13-z_10*y_13)==0), Not((z_10*x_13-x_10*z_13)==0), Not((x_10*y_13-y_10*x_13)==0))) 
    s.add(Or(Not((y_11*z_13-z_11*y_13)==0), Not((z_11*x_13-x_11*z_13)==0), Not((x_11*y_13-y_11*x_13)==0))) 
    s.add(((z_2*x_6-x_2*z_6)*z_8-(x_2*y_6-y_2*x_6)*y_8)==0) 
    s.add(((x_2*y_6-y_2*x_6)*x_8-(y_2*z_6-z_2*y_6)*z_8)==0) 
    s.add(((y_2*z_6-z_2*y_6)*y_8-(z_2*x_6-x_2*z_6)*x_8)==0) 
    s.add(((z_1*x_3-x_1*z_3)*z_9-(x_1*y_3-y_1*x_3)*y_9)==0) 
    s.add(((x_1*y_3-y_1*x_3)*x_9-(y_1*z_3-z_1*y_3)*z_9)==0) 
    s.add(((y_1*z_3-z_1*y_3)*y_9-(z_1*x_3-x_1*z_3)*x_9)==0) 
    s.add(((z_0*x_7-x_0*z_7)*z_10-(x_0*y_7-y_0*x_7)*y_10)==0) 
    s.add(((x_0*y_7-y_0*x_7)*x_10-(y_0*z_7-z_0*y_7)*z_10)==0) 
    s.add(((y_0*z_7-z_0*y_7)*y_10-(z_0*x_7-x_0*z_7)*x_10)==0) 
    s.add(((z_3*x_4-x_3*z_4)*z_11-(x_3*y_4-y_3*x_4)*y_11)==0) 
    s.add(((x_3*y_4-y_3*x_4)*x_11-(y_3*z_4-z_3*y_4)*z_11)==0) 
    s.add(((y_3*z_4-z_3*y_4)*y_11-(z_3*x_4-x_3*z_4)*x_11)==0) 
    s.add(((z_4*x_5-x_4*z_5)*z_12-(x_4*y_5-y_4*x_5)*y_12)==0) 
    s.add(((x_4*y_5-y_4*x_5)*x_12-(y_4*z_5-z_4*y_5)*z_12)==0) 
    s.add(((y_4*z_5-z_4*y_5)*y_12-(z_4*x_5-x_4*z_5)*x_12)==0) 
    s.add(((z_5*x_6-x_5*z_6)*z_13-(x_5*y_6-y_5*x_6)*y_13)==0) 
    s.add(((x_5*y_6-y_5*x_6)*x_13-(y_5*z_6-z_5*y_6)*z_13)==0) 
    s.add(((y_5*z_6-z_5*y_6)*y_13-(z_5*x_6-x_5*z_6)*x_13)==0) 
    s.add(x_2 == 0) 
    s.add(y_2 == 0) 
    s.add(z_2 == 1) 
    s.add(x_6 == 0) 
    s.add(y_6 == 1) 
    s.add(z_6 == 0) 
    s.add(x_8 == 1) 
    s.add(y_8 == 0) 
    s.add(z_8 == 0) 
    return (s.check()) 
print(test_embed())