def write_ascii_triangle(triangle_doc, block, sidelength):
    """ (File Open for writing, str, int) -> NoneType
    
    Precondition: len(block) == 1
    
    Write an ascii isosceles right triangle of character block that is
    sidelength characters wide and high to triangle_doc. The right
    angle should be in the upper-left corner. For example, given
    block="@" and sidelength=4, the following should be written to triangle_doc:
    
    @@@@
    @@@
    @@
    @
    """
    
    columns = sidelength
    for row in range(sidelength):
        for column in range(columns):
            triangle_doc.write(block)
        triangle_doc.write('\n')
        columns -= 1
    