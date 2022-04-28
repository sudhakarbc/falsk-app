import logo from './logo.svg';
import React, { useEffect,useState } from 'react';
import {ListGroup, Badge,Container,Row,Col} from 'react-bootstrap';



function App() {
  
    useEffect(() => {
      // let mounted = true;
  
      // if(mounted) {
      fetch('/list-s3').then(res => res.json()).then(data => {
            setBuckets(data);
            console.log("Updated buckets");
          });
      fetch('/list-available-volumes').then(res => res.json()).then(data => {
          console.log(data)
  
        })
      // }
    //  return () => mounted = false;
  
      }, []);
  const [buckets,setBuckets] = useState([]);




  return (

    <Container>  
    <Row className="m-1 p-1">  
      <Col>
        <ListGroup as="ol" numbered>
          {buckets.map((bucket,i) => (
            <ListGroup.Item
              as="li"
              className="d-flex justify-content-between align-items-start"
              key={i}
            >
              <div className="ms-2 me-auto">
                <div className="fw-bold">{bucket.name}</div>
              </div>
              <Badge bg="primary" pill>
              {bucket.size}
              </Badge>
            </ListGroup.Item>
            
          ))}
        </ListGroup>
      </Col>  
    </Row>  
  </Container>  

  
  );
}

export default App;
