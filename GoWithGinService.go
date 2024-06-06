// main.go

package main

import (
	"log"
	"net/http"
	"time"

	"github.com/gin-gonic/gin"
)

// Customer struct represents customer details
type Customer struct {
	Name string `json:"name"`
	Code string `json:"code"`
}

// Order struct represents order details
type Order struct {
	Item   string    `json:"item"`
	Amount float64   `json:"amount"`
	Time   time.Time `json:"time"`
}

// Dummy data storage
var customers []Customer
var orders []Order

func main() {
	router := gin.Default()

	// Routes for customers
	router.GET("/customers", getCustomers)
	router.POST("/customers", createCustomer)

	// Routes for orders
	router.GET("/orders", getOrders)
	router.POST("/orders", createOrder)

	// Run the server
	if err := router.Run(":8080"); err != nil {
		log.Fatal(err)
	}
}

// Handler to get all customers
func getCustomers(c *gin.Context) {
	c.JSON(http.StatusOK, customers)
}

// Handler to create a new customer
func createCustomer(c *gin.Context) {
	var customer Customer
	if err := c.BindJSON(&customer); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	customers = append(customers, customer)
	c.JSON(http.StatusCreated, customer)
}

// Handler to get all orders
func getOrders(c *gin.Context) {
	c.JSON(http.StatusOK, orders)
}

// Handler to create a new order
func createOrder(c *gin.Context) {
	var order Order
	if err := c.BindJSON(&order); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	order.Time = time.Now()
	orders = append(orders, order)
	// Send SMS alert here
	sendSMSAlert(order)
	c.JSON(http.StatusCreated, order)
}

// Dummy function to simulate sending SMS alert
func sendSMSAlert(order Order) {
	log.Printf("SMS Alert: New order added - Item: %s, Amount: %.2f, Time: %s", order.Item, order.Amount, order.Time.Format(time.RFC3339))
}
