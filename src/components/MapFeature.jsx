import React, { useState, useCallback, useEffect } from "react";
import { GoogleMap, useJsApiLoader, Marker, InfoWindow } from "@react-google-maps/api";
import festivals from "../data/festivals.json";
import FestivalDetails from "./FestivalDetails";

const containerStyle = {
    width: "100%",
    height: "60vh",
    borderRadius: "12px",
    boxShadow: "0 4px 6px rgba(0,0,0,0.1)",
    marginTop: "20px"
};

const center = {
    lat: 25.0961, // Default roughly center of Bihar
    lng: 85.3131,
};

function MapFeature() {
    const { isLoaded } = useJsApiLoader({
        id: "google-map-script",
        googleMapsApiKey: process.env.REACT_APP_GOOGLE_MAPS_API_KEY,
    });

    const [map, setMap] = useState(null);
    const [activeMarker, setActiveMarker] = useState(null);
    const [userLocation, setUserLocation] = useState(center);
    const [selectedFestival, setSelectedFestival] = useState(null);

    const onLoad = useCallback(function callback(map) {
        setMap(map);
    }, []);

    const onUnmount = useCallback(function callback(map) {
        setMap(null);
    }, []);

    // Fetch user location
    useEffect(() => {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(
                (position) => {
                    setUserLocation({
                        lat: position.coords.latitude,
                        lng: position.coords.longitude,
                    });
                },
                () => {
                    console.warn("Geolocation permission denied or not available. Using default center.");
                }
            );
        }
    }, []);

    if (selectedFestival) {
        return <FestivalDetails festival={selectedFestival} onBack={() => setSelectedFestival(null)} />;
    }

    return (
        <div className="map-feature" style={{ padding: "20px" }}>
            <h1 className="main-title">Interactive Festival Map</h1>
            <p style={{ textAlign: "center", marginBottom: "10px" }}>
                Discover festivals happening nearby. Click on markers for details!
            </p>

            {isLoaded ? (
                <GoogleMap
                    mapContainerStyle={containerStyle}
                    center={userLocation}
                    zoom={7}
                    onLoad={onLoad}
                    onUnmount={onUnmount}
                    options={{
                        disableDefaultUI: false,
                        zoomControl: true,
                    }}
                >
                    {/* User Location Marker */}
                    <Marker
                        position={userLocation}
                        icon={{
                            url: "http://maps.google.com/mapfiles/ms/icons/blue-dot.png",
                        }}
                        title="Your Location"
                    />

                    {/* Festival Markers */}
                    {festivals.map((fest) => (
                        <Marker
                            key={fest.id}
                            position={{ lat: fest.lat, lng: fest.lng }}
                            onClick={() => setActiveMarker(fest.id)}
                        >
                            {activeMarker === fest.id && (
                                <InfoWindow onCloseClick={() => setActiveMarker(null)}>
                                    <div style={{ padding: "5px", maxWidth: "200px" }}>
                                        <h3 style={{ margin: "0 0 5px 0", fontSize: "16px", color: "#1e3a8a" }}>{fest.festivalName}</h3>
                                        <p style={{ margin: "0 0 5px 0", fontSize: "12px" }}>
                                            <b>Dates:</b> {fest.startDate} to {fest.endDate}
                                        </p>
                                        <p style={{ margin: "0 0 10px 0", fontSize: "12px" }}>{fest.shortInfo.why}</p>
                                        <button
                                            className="primary-btn"
                                            style={{ padding: "5px 10px", fontSize: "12px" }}
                                            onClick={() => {
                                                if (fest.externalLink) {
                                                    window.open(fest.externalLink, "_blank");
                                                } else {
                                                    setSelectedFestival(fest);
                                                }
                                            }}
                                        >
                                            Read More {fest.externalLink && "↗"}
                                        </button>
                                    </div>
                                </InfoWindow>
                            )}
                        </Marker>
                    ))}
                </GoogleMap>
            ) : (
                <p style={{ textAlign: "center" }}>Loading Map...</p>
            )}
        </div>
    );
}

export default React.memo(MapFeature);
