import "./ImageModal.css";

function ImageModal({ image, title, onClose }) {

    if (!image) return null;

    return (

        <div className="modal-overlay" onClick={onClose}>

            <div
                className="modal-content"
                onClick={(e) => e.stopPropagation()}
            >

                <button
                    className="close-btn"
                    onClick={onClose}
                >
                    ✕
                </button>

                <h2>{title}</h2>

                <img
                    src={image}
                    alt={title}
                    className="modal-image"
                />

            </div>

        </div>

    );

}

export default ImageModal;