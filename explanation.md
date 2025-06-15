# Mathematical Description

The movement of the sun across the sky during the day is the result of two effects: the rotation of the Earth around its axis and the revolution of the Earth around the sun. The latter effect, combined with the fact that the Earth's axis is not perpendicular to the plane of revolution, influences the trajectory to be different at different times of the year. However, during the period of one day, Earth's relative position with respect to the Sun changes only slightly, and its effect is negligible compared to Earth's rotation.

To quantitatively describe the Sun's movement in the sky, we first need to define a coordinate system. We'll take the Earth's center as the origin of the coordinate system, and the Earth's axis of rotation as the $z$-axis. The direction of the sun (which we assume to be constant for the duration of one day) can be represented as a unit vector $\hat{s}$ pointing towards the sun. At any time of the year, this vector can be broken down into two components: one parallel to the Earth's axis of rotation, and the other perpendicular to it. We set the $x$-axis to be in the direction of the perpendicular component, and the $y$-axis is chosen such that these axes form a right-handed coordinate system. Note that in this coordinate system, $\hat{s}$ has zero $y$ component.

Furthermore, we can describe a point on Earth's surface using two angles: the angle between the $xy$-plane and the vector from the origin to the point, and the angle between the $x$-axis and the projection of the vector onto the $xy$-plane. The former is known as latitude (the latter is not longitude; longitude is the angle between the meridian on which this point lies and the Greenwich meridian). Moreover, each point on the surface of the Earth has its own local coordinate system, with axes pointing toward zenith, north, and east. This coordinate system rotates with Earth, and the rotation is what causes the apparent movement of the sun across the sky. The sun's position in the sky can also be described using angles: the angle between the sun and the horizon, known as altitude, and the angle between the sun and the north, known as azimuth.

Let's proceed with the mathematics. Given an angle $\alpha$ between the plane of revolution and the $xy$-plane (or equivalently, an angle between Earth's moment of impulse with respect to the Sun and Earth's axis of rotation), also known as declination, we can express the sun's direction as:

$$\begin{equation}
\hat{s} = \cos{\alpha} \hat{x} + \sin{\alpha} \hat{z}
\end{equation}$$

The unit vectors of the local coordinate system can be expressed as:

$$\begin{align*}
\hat{r} &= \cos{\theta}\sin{\phi} \hat{x} + \cos{\theta}\cos{\phi} \hat{y} + \sin{\theta} \hat{z} \\
\hat{\theta} &= \frac{\partial\hat{r}}{\partial\theta} \\
\hat{\phi} &= \frac{\partial\hat{r}}{\partial\phi}
\end{align*}$$

The Sun's coordinates in the local coordinate system are then:

$$\begin{align*}
\hat{s}\cdot \hat{r} &= \cos{\alpha}\cos{\theta}\cos{\phi} + \sin{\alpha}\sin{\theta} \\
\hat{s}\cdot \hat{\theta} &= \hat{s}\cdot \frac{\partial\hat{r}}{\partial\theta} = \frac{\partial}{\partial\theta}(\hat{r}\cdot \hat{s}) \\ &= -\cos{\alpha}\sin{\theta}\cos{\phi} + \sin{\alpha}\cos{\theta} \\
\hat{s}\cdot \hat{\phi} &= \hat{s}\cdot \frac{\partial\hat{r}}{\partial\phi} = \frac{\partial }{\partial\phi} \frac{\partial}{\partial\phi}(\hat{r}\cdot \hat{s}) \\ &= -\cos{\alpha}\cos{\theta}\sin{\phi}
\end{align*}$$

Altitude and azimuth can be expressed as:

$$\begin{align*}
\text{altitude} &= \arcsin{\hat{s}\cdot \hat{r}} \\
\text{azimuth} &= \arctan{\left(\frac{\hat{s}\cdot \hat{\phi}}{\hat{s}\cdot \hat{\theta}}\right)}
\end{align*}$$

Since $\phi$ changes from $-\pi$ to $\pi$ during one day, the altitude and azimuth are functions of time, latitude, and declination.

This framework allows us to analytically describe the sun's apparent motion for any location and time of year.



