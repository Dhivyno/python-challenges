import turtle

def draw_decision_tree(t, question, true_branch, false_branch):
    t.write(question, align='center')
    true_pos = list(t.position())
    print(true_pos[0])
    true_pos[0] += 50
    true_pos[1] -= 50
    false_pos = list(t.position())
    false_pos[0] -= 50
    false_pos[1] -= 50
    t.pendown()
    t.goto(true_pos)
    t.penup()
    t.goto(false_pos)
    t.penup()
    draw_decision_tree(t, true_branch[0], true_branch[1], true_branch[2])
    draw_decision_tree(t, false_branch[0], false_branch[1], false_branch[2])
  
t = turtle.Turtle()
t.speed(0)
draw_decision_tree(t, 'Is it raining?', ('Yes', ('Bring an umbrella', None, None), ('Wear a raincoat', None, None)), ('No', ('Go for a walk', None, None), ('Stay inside', None, None)))
turtle.done()
