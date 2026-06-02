# 1. Define aquí los puertos que quieres revisar
$puertos = @(80, 443, 135, 8080, 3306)

# 2. Ejecuta el buscador
$resultado = foreach ($puerto in $puertos) {
    $conexion = Get-NetTCPConnection -LocalPort $puerto -ErrorAction SilentlyContinue | Select-Object -First 1
    if ($conexion) {
        $proceso = Get-Process -Id $conexion.OwningProcess -ErrorAction SilentlyContinue
        [PSCustomObject]@{
            Puerto      = $puerto
            PID         = $conexion.OwningProcess
            Programa    = $proceso.Name
            Ruta        = $proceso.Path
            Estado      = $conexion.State
        }
    } else {
        [PSCustomObject]@{
            Puerto      = $puerto
            PID         = "Libre"
            Programa    = "-"
            Ruta        = "-"
            Estado      = "-"
        }
    }
}

# 3. Muestra el resultado en una tabla bonita
$resultado | Format-Table -AutoSize
