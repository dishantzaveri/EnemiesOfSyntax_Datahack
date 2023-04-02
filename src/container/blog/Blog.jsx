import React from "react";
import "./Blog.css";
import { useState } from "react";

function ImageBlog() {
  const [images, setImages] = useState({});
  const [answers, setAnswers] = useState(Array(5).fill(""));

  const handleImageUpload = (event) => {
    const uploadedImages = event.target.files[0];
    setImages((x) => ({ [event.target.name]: uploadedImages, ...x }));
  };

  const handleAnswerChange = (event, index) => {
    const newAnswers = [...answers];
    newAnswers[index] = event.target.value;
    setAnswers(newAnswers);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log({ images, answers });
  };

  return (
    <div className="blog-page">
      <button onSubmit={handleSubmit}>
        <h2 className="images__y">Upload 5 Images</h2>
        <div className="align-center">
          <ol className="questions__y">
            <li>
              <label htmlFor="question-1">Front view of the car</label>
              <input
                className="image__input"
                type="file"
                accept="image/*"
                multiple
                onChange={handleImageUpload}
                name="image_1"
              />
            </li>
            <li>
              <label htmlFor="question-2">LHS view</label>
              <input
                className="image__input"
                type="file"
                accept="image/*"
                multiple
                onChange={handleImageUpload}
                name="image_2"
              />
            </li>
            <li>
              <label htmlFor="question-3">RHS</label>
              <input
                className="image__input"
                type="file"
                accept="image/*"
                multiple
                onChange={handleImageUpload}
                name="image_3"
              />
            </li>
            <li>
              <label htmlFor="question-4">back view</label>
              <input
                className="image__input"
                type="file"
                accept="image/*"
                multiple
                onChange={handleImageUpload}
                name="image_4"
              />
            </li>
            <li>
              <label htmlFor="question-5">diagonal view</label>
              <input
                className="image__input"
                type="file"
                accept="image/*"
                multiple
                onChange={handleImageUpload}
                name="image_5"
              />
            </li>
          </ol>
        </div>

        <h2 className="images__y">Answer 5 Questions</h2>
        <ol className="questions__y">
          <li>
            <label htmlFor="question-1">Question 1:</label>
            <input
              className="question__input"
              type="text"
              id="question-1"
              value={answers[0]}
              onChange={(event) => handleAnswerChange(event, 0)}
              name="q_1"
            />
          </li>
          <li>
            <label htmlFor="question-2">Question 2:</label>
            <input
              className="question__input"
              type="text"
              id="question-2"
              value={answers[1]}
              onChange={(event) => handleAnswerChange(event, 1)}
              name="q_2"
            />
          </li>
          <li>
            <label htmlFor="question-3">Question 3:</label>
            <input
              className="question__input"
              type="text"
              id="question-3"
              value={answers[2]}
              onChange={(event) => handleAnswerChange(event, 2)}
              name="q_3"
            />
          </li>
          <li>
            <label htmlFor="question-4">Question 4:</label>
            <input
              className="question__input"
              type="text"
              id="question-4"
              value={answers[3]}
              onChange={(event) => handleAnswerChange(event, 3)}
              name="q_4"
            />
          </li>
          <li>
            <label htmlFor="question-5">Question 5:</label>
            <input
              className="question__input"
              type="text"
              id="question-5"
              value={answers[4]}
              onChange={(event) => handleAnswerChange(event, 4)}
              name="q_5"
            />
          </li>
        </ol>
        <button className="images__x" type="submit">
          Submit
        </button>
      </button>
    </div>
  );
}

export default ImageBlog;
// import { useState } from "react";
// import React from "react";
// import { PhotoIcon, UserCircleIcon } from "@heroicons/react/24/solid";
// function Blog() {
//   const [images, setImages] = useState(null);
//   const [answers, setAnswers] = useState(Array(5).fill(""));

//   const handleImageUpload = (event) => {
//     const uploadedImages = event.target.files[0];
//     setImages((x) => ({ [event.target.name]: uploadedImages, ...x }));
//     console.log(images);
//   };

//   const handleAnswerChange = (event, index) => {
//     const newAnswers = [...answers];
//     newAnswers[index] = event.target.value;
//     setAnswers(newAnswers);
//   };

//   const handleSubmit = (event) => {
//     event.preventDefault();
//     console.log({ images, answers });
//   };

//   return (
//     <>
//       <div className="grid grid-cols-1">
//         <div className="">
//           <label
//             htmlFor="cover-photo"
//             className="block text-sm font-medium leading-6 text-white"
//           >
//             Front View
//           </label>
//           <div className="mt-2 flex justify-center rounded-lg border border-dashed border-white ">
//             <div className="text-center">
//               <PhotoIcon
//                 className="mx-auto h-5 w-5 text-white"
//                 aria-hidden="true"
//               />
//               <div className="mt-4 flex text-sm leading-6 text-white">
//                 <label
//                   htmlFor="file-upload"
//                   className="relative cursor-pointer rounded-md bg-white font-semibold text-indigo-600 focus-within:outline-none focus-within:ring-2 focus-within:ring-indigo-600 focus-within:ring-offset-2 hover:text-indigo-500"
//                 >
//                   {" "}
//                   <input
//                     className="image__input"
//                     type="file"
//                     accept="image/*"
//                     multiple
//                     onChange={(e) => setImages(e.target.files[0])}
//                     name="image_1"
//                   />
//                 </label>
//                 <p className="pl-1">or drag and drop</p>
//               </div>
//               <p className="text-xs leading-5 text-white">
//                 PNG, JPG, GIF up to 10MB
//               </p>
//               {images && (
//                 <img src={URL.createObjectURL(images)} alt="Uploaded Image" />
//               )}
//             </div>
//           </div>
//         </div>
//         <div className="">
//           <label
//             htmlFor="cover-photo"
//             className="block text-sm font-medium leading-6 text-white"
//           >
//             Left hand side View
//           </label>
//           <div className="mt-2 flex justify-center rounded-lg border border-dashed border-white ">
//             <div className="text-center">
//               <PhotoIcon
//                 className="mx-auto h-5 w-5 text-white"
//                 aria-hidden="true"
//               />
//               <div className="mt-4 flex text-sm leading-6 text-white">
//                 <label
//                   htmlFor="file-upload"
//                   className="relative cursor-pointer rounded-md bg-white font-semibold text-indigo-600 focus-within:outline-none focus-within:ring-2 focus-within:ring-indigo-600 focus-within:ring-offset-2 hover:text-indigo-500"
//                 >
//                   <span>Upload a file</span>
//                   {/* <input
//                     id="file-upload"
//                     name="file-upload"
//                     type="file"
//                     className="sr-only"
//                   /> */}
//                   <input
//                     className="image__input"
//                     type="file"
//                     accept="image/*"
//                     multiple
//                     onChange={(e) => setImages(e.target.files[0])}
//                     name="image_2"
//                   />
//                 </label>
//                 <p className="pl-1">or drag and drop</p>
//               </div>
//               <p className="text-xs leading-5 text-white">
//                 PNG, JPG, GIF up to 10MB
//               </p>
//             </div>
//           </div>
//         </div>

//         <div className="">
//           <label
//             htmlFor="cover-photo"
//             className="block text-sm font-medium leading-6 text-white"
//           >
//             Right hand side View
//           </label>
//           <div className="mt-2 flex justify-center rounded-lg border border-dashed border-white ">
//             <div className="text-center">
//               <PhotoIcon
//                 className="mx-auto h-12 w-12 text-white"
//                 aria-hidden="true"
//               />
//               <div className="mt-4 flex text-sm leading-6 text-white">
//                 <label
//                   htmlFor="file-upload"
//                   className="relative cursor-pointer rounded-md bg-white font-semibold text-indigo-600 focus-within:outline-none focus-within:ring-2 focus-within:ring-indigo-600 focus-within:ring-offset-2 hover:text-indigo-500"
//                 >
//                   <span>Upload a file</span>
//                   <input
//                     // id="file-upload"
//                     // name="file-upload"
//                     // type="file"
//                     // className="sr-only"
//                     className="image__input"
//                     type="file"
//                     accept="image/*"
//                     multiple
//                     onChange={(e) => setImages(e.target.files[0])}
//                     name="image_3"
//                   />
//                 </label>
//                 <p className="pl-1">or drag and drop</p>
//               </div>
//               <p className="text-xs leading-5 text-white">
//                 PNG, JPG, GIF up to 10MB
//               </p>
//             </div>
//           </div>
//         </div>
//         <div className="">
//           <label
//             htmlFor="cover-photo"
//             className="block text-sm font-medium leading-6 text-white"
//           >
//             Back View
//           </label>
//           <div className="mt-2 flex justify-center rounded-lg border border-dashed border-white ">
//             <div className="text-center">
//               <PhotoIcon
//                 className="mx-auto h-12 w-12 text-white"
//                 aria-hidden="true"
//               />
//               <div className="mt-4 flex text-sm leading-6 text-white">
//                 <label
//                   htmlFor="file-upload"
//                   className="relative cursor-pointer rounded-md bg-white font-semibold text-indigo-600 focus-within:outline-none focus-within:ring-2 focus-within:ring-indigo-600 focus-within:ring-offset-2 hover:text-indigo-500"
//                 >
//                   <span>Upload a file</span>
//                   <input
//                     // id="file-upload"
//                     // name="file-upload"
//                     // type="file"
//                     // className="sr-only"
//                     className="image__input"
//                     type="file"
//                     accept="image/*"
//                     multiple
//                     onChange={(e) => setImages(e.target.files[0])}
//                     name="image_4"
//                   />
//                 </label>
//                 <p className="pl-1">or drag and drop</p>
//               </div>
//               <p className="text-xs leading-5 text-white">
//                 PNG, JPG, GIF up to 10MB
//               </p>
//             </div>
//           </div>
//         </div>
//         <div className="">
//           <label
//             htmlFor="cover-photo"
//             className="block text-sm font-medium leading-6 text-white"
//           >
//             Diagonal View
//           </label>
//           <div className="mt-2 flex justify-center rounded-lg border border-dashed border-white ">
//             <div className="text-center">
//               <PhotoIcon
//                 className="mx-auto h-12 w-12 text-white"
//                 aria-hidden="true"
//               />
//               <div className="mt-4 flex text-sm leading-6 text-white">
//                 <label
//                   htmlFor="file-upload"
//                   className="relative cursor-pointer rounded-md bg-white font-semibold text-indigo-600 focus-within:outline-none focus-within:ring-2 focus-within:ring-indigo-600 focus-within:ring-offset-2 hover:text-indigo-500"
//                 >
//                   <span>Upload a file</span>
//                   <input
//                     // id="file-upload"
//                     // name="file-upload"
//                     // type="file"
//                     // className="sr-only"
//                     className="image__input"
//                     type="file"
//                     accept="image/*"
//                     multiple
//                     onChange={(e) => setImages(e.target.files[0])}
//                     name="image_5"
//                   />
//                 </label>
//                 <p className="pl-1">or drag and drop</p>
//               </div>
//               <p className="text-xs leading-5 text-white">
//                 PNG, JPG, GIF up to 10MB
//               </p>
//             </div>
//           </div>
//         </div>
//       </div>
//       <div className="p-5">
//         <label
//           class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2 pt-5"
//           for="grid-first-name"
//         >
//           First Name
//         </label>
//         <label
//           class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2 pt-5"
//           for="grid-first-name"
//         >
//           First Name
//         </label>
//         <label
//           class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2 pt-5"
//           for="grid-first-name"
//         >
//           First Name
//         </label>
//         <label
//           class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2 pt-5"
//           for="grid-first-name"
//         >
//           First Name
//         </label>
//         <label
//           class="block uppercase tracking-wide text-gray-700 text-xs font-bold mb-2 pt-5"
//           for="grid-first-name"
//         >
//           First Name
//         </label>
//       </div>
//     </>
//   );
// }

// export default Blog;
