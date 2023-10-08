
import React,{ useEffect, useState } from "react";
import { BuilderComponent, builder, useIsPreviewing, Builder } from "@builder.io/react";
import Heading from "./Heading";

// Put your API key here
builder.init('33f040e0f6b744819dd3f3aad5bb7539');
// Set the builderSessionId cookie
// document.cookie = "SameSite=None; Secure";

// // Make sure that every page where renders Builder 
// // content calls the file containing this function call
Builder.registerComponent(Heading, { 
  name: 'Heading',
  inputs: [{ name: 'title', type: 'text' }],
  image: 'https://tabler-icons.io/static/tabler-icons/icons-png/3d-cube-sphere-off.png'
})
// set whether you're using the Visual Editor,
// whether there are changes,
// and render the content if found
export default function CatchAllRoute() {
  const isPreviewingInBuilder = useIsPreviewing();
  const [notFound, setNotFound] = useState(false);
  const [content, setContent] = useState(null);

  // get the page content from Builder
   useEffect(() => {
    async function fetchContent() {
      const content = await builder
        .get("page", {
          url: window.location.pathname
        })
        .promise();

      setContent(content);
      setNotFound(!content);

      // if the page title is found, 
      // set the document title
      if (content?.data.title) {
       document.title = content.data.title
      }
    }
    fetchContent();
  }, [window.location.pathname]);
  
  // If no page is found, return 
  // a 404 page from your code.
  // The following hypothetical 
  // <FourOhFour> is placeholder.
  // if (notFound && !isPreviewingInBuilder) {
  //   return <FourOhFour/>
  // }

  // return the page when found
  return (
    <>
      {/* Render the Builder page */}
      <BuilderComponent model="page" content={content} />
    </>
  );
}





