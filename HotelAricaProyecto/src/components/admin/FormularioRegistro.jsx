import React from 'react'

export const FormularioRegistro = () => {
  return (
    <section>
      <h2>FormularioRegistro</h2>
      <form>
        <div className="form-group">
          <label htmlFor="nombre">Nombre</label>
          <input className='form-control' type="text" id='nombre'/>
        </div>
      </form>
    </section>
  )
}