class Vector2:
    """	
    	二维向量计算: 仅做为Tips。
    """
    def __init__(self, x, y):
        self.x = x or 0
        self.y = y or 0

    def __str__(self):
        return 'Vector2(%f,%f)' %(self.x,self.y)

    __repr__ = __str__

    def cross2D(self, v):
        """	
        功能说明：和向量v进行叉乘。
        
        向量积|c|=|a×b|=|a|*|b|*sin<a,b>
        即c的长度在数值上等于以a，b，夹角为θ组成的平行四边形的面积。
        而c的方向垂直于a与b所决定的平面，c的指向按右手定则从a转向b来确定。
        
        返回:叉乘向量
        """

        pass

    def distSqrTo(self, p):
        """	
        功能说明：到点p 的距离的平方。
        返回: float
        """
        pass

    def distTo(self, p):
        """	
        功能说明：到点p 的距离。
        返回: float
        """
        pass

    def dot(self, v):
        """	
        功能说明：和向量v进行点乘。 a·b=|a|*|b|*cos<a,b>
        返回: float
        """
        pass

    def length(self):
        """	
        功能说明：向量的长度：sqrt(x*x+y*y)
        返回: float
        """
        pass

    def lengthSquared(self):
        """	
        功能说明：向量的长度的平方：x*x+y*y
        返回: float
        """
        pass

    def list(self):
        """	
        功能说明：转换为列表list
        返回列表
        """
        pass

    def normalise(self):
        """	
        功能说明：单位化。 修改self。
        无返回值
        """
        pass

    def tuple(self):
        """	
        功能说明：转换为元组tuple
        返回元组
        """
        pass

    def scale(self, s):
        """	
        功能说明：返回新的向量（self.x*s,self.y*s），不修改self的值。
        返回新的向量
        """
        pass

    def set(self, x, y):
        """	
        功能说明：设置self的新值
        无返回值
        """
        pass


class Vector3:
    """	
     三维向量计算: 仅做为Tips。
    """

    def __init__(self, x, y, z):
        self.x = x or 0
        self.y = y or 0
        self.z = z or 0

    def __str__(self):
        return 'Vector3(%f,%f,%f)' %(self.x,self.y,self.z)

    __repr__ = __str__

    def cross2D(self, v):
        """	
        功能说明：和向量v进行叉乘。

        向量积|c|=|a×b|=|a|*|b|*sin<a,b>
        即c的长度在数值上等于以a，b，夹角为θ组成的平行四边形的面积。
        而c的方向垂直于a与b所决定的平面，c的指向按右手定则从a转向b来确定。

        返回:叉乘向量
        """

        pass

    def distSqrTo(self, p):
        """	
        功能说明：到点p 的距离的平方。
        返回: float
        """
        pass

    def distTo(self, p):
        """	
        功能说明：到点p 的距离。
        返回: float
        """
        pass

    def dot(self, v):
        """	
        功能说明：和向量v进行点乘。 a·b=|a|*|b|*cos<a,b>
        返回: float
        """
        pass

    def length(self):
        """	
        功能说明：向量的长度：sqrt(x*x+y*y)
        返回: float
        """
        pass

    def lengthSquared(self):
        """	
        功能说明：向量的长度的平方：x*x+y*y
        返回: float
        """
        pass

    def list(self):
        """	
        功能说明：转换为列表list
        返回列表
        """
        pass

    def normalise(self):
        """	
        功能说明：单位化。 修改self。
        无返回值
        """
        pass

    def tuple(self):
        """	
        功能说明：转换为元组tuple
        返回元组
        """
        pass

    def scale(self, s):
        """	
        功能说明：返回新的向量（self.x*s,self.y*s），不修改self的值。
        返回新的向量
        """
        pass

    def set(self, x, y, z):
        """	
        功能说明：设置self的新值
        无返回值
        """
        pass

    def flatDistSqrTo(self, p):
        """	
        功能说明：在xz平面上，到点p 的距离的平方。 self.xz.distSqrTo(p.xz)
        返回: float
        """
        pass

    def flatDistTo(self, p):
        """	
        功能说明：在xz平面上，到点p 的距离。 self.xz.distTo(p.xz)
        返回: float
        """
        pass


class Vector4:
    """	
    	四维向量计算: 仅做为Tips。
    """

    def __init__(self, x, y, z, w):
        self.x = x or 0
        self.y = y or 0
        self.z = z or 0
        self.w = w or 0

    def __str__(self):
        return 'Vector4(%f,%f,%f,%f)' %(self.x,self.y,self.z,self.w)

    __repr__ = __str__

    def distSqrTo(self, p):
        """	
        功能说明：到点p 的距离的平方。
        返回: float
        """
        pass

    def distTo(self, p):
        """	
        功能说明：到点p 的距离。
        返回: float
        """
        pass

    def dot(self, v):
        """	
        功能说明：和向量v进行点乘。 a·b=|a|*|b|*cos<a,b>
        返回: float
        """
        pass

    def length(self):
        """	
        功能说明：向量的长度：sqrt(x*x+y*y)
        返回: float
        """
        pass

    def lengthSquared(self):
        """	
        功能说明：向量的长度的平方：x*x+y*y
        返回: float
        """
        pass

    def list(self):
        """	
        功能说明：转换为列表list
        返回列表
        """
        pass

    def normalise(self):
        """	
        功能说明：单位化。 修改self。
        无返回值
        """
        pass

    def tuple(self):
        """	
        功能说明：转换为元组tuple
        返回元组
        """
        pass

    def scale(self, s):
        """	
        功能说明：返回新的向量（self.x*s,self.y*s），不修改self的值。
        返回新的向量
        """
        pass

    def set(self, x, y, z, w):
        """	
        功能说明：设置self的新值
        无返回值
        """
        pass