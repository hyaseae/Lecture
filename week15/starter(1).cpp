#include <iostream>
#include <vector>
#include <string>
#include <memory>


class Shape {
protected:
    std::string color;
    
public:
    // TASK 1: Implement the constructor to initialize the 'color' attribute.
    Shape(std::string color_in) : color(color_in)
    {

    }
    
    // TASK 2: Define the pure virtual function for drawing, named 'draw'.


    virtual void draw() = 0;
    
    // TASK 3. Define a virtual destructor.
    // Inside, print: "Base (Shape) destructor for 'color'.

    virtual ~Shape()
    {
        std::cout << "Base (Shape) destructor for '" << color << "'.\n";
    }


};


class Circle : public Shape {
private:
    double radius;
    
public:
    // TASK 4: Implement the Circle constructor. It must call the Base (Shape) constructor.

    Circle(std::string color_in, double radius_) : Shape(color_in), radius(radius_)
    {

    };
    // TASK 5: Implement the 'draw' function, using the 'override' keyword.
    // Inside, print: "'color' circle with radius 'radius'."

    void draw() override {
        std::cout << "'" << color << "' circle with radius '" << radius << "'.\n";
    }

    
    // TASK 6: Include a derived destructor.
    // Inside, print: "Circle destructor."

    ~Circle() {
        std::cout << "Circle destructor.\n";
    };
};


class Rectangle : public Shape {
private:
    double width, height;
    
public:
    // TASK 7: Implement the Rectangle constructor, calling the Base (Shape) constructor.
    Rectangle(std::string color_in, double width_, double height_) : Shape(color_in), width(width_), height(height_)
    {

    }
    
    // TASK 8: Implement the 'draw' function, using the 'override' keyword.
    // Inside, print: "'color' rectangle ('width' x 'height')."
    void draw() override {
        std::cout << "'" << color << "' rectangle ('" << width << "' x '" << height << "').\n";
    }
    
    // TASK 9: Include a derived destructor.
    // Inside, print: "Rectangle destructor."

    ~Rectangle()
    {
        std::cout << "Rectangle destructor.\n";
    }

};


int main() {
    std::vector<std::unique_ptr<Shape>> canvas;

    // TASK 10: Create a "Red" Circle (with radius 5.0) and add its pointer to the canvas.
    // Use std::make_unique and push_back functions.
    std::unique_ptr<Shape> p_c = std::make_unique<Circle>("Red", 5.0);
    
    // TASK 11: Create a "Blue" Rectangle (10.0 x 8.0) and add its pointer to the canvas.
    std::unique_ptr<Shape> p_r = std::make_unique<Rectangle>("Blue", 10.0, 8.0);




    for (const auto& s : canvas) {
        // TASK 12: Call the draw method polymorphically.
        s->draw();
    }

    Shape* p_ = new Circle("black", 1.0);

    delete p_;


    canvas.clear();

    return 0;
}
