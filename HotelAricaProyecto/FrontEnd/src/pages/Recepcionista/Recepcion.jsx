import React from 'react'

import { Habitaciones } from '../../components/Recepcionista/recepcion/Habitaciones'
import './styles.css'
export const Recepcion = () => {

 
  return (
    <>
      <section className='container fondo-recepcion' >
        <div className="d-flex align-items-center justify-content-left gap-3  pt-4">
          <div style={{fontSize: '40px'}} className='d-flex align-items-center p-0 m-0'>
            <img width='40px' src="https://cdn-icons-png.flaticon.com/128/3313/3313488.png" alt="Esto es una imagen de un icono" />
          </div>
          <h1 className='m-0'>Modulo de Recepcion</h1>
        </div>
        <div className="row mt-3">
          <div className="col-md-12">
            <Habitaciones/>
          </div>
          
        </div>
      </section>

    </>
    
  )
}